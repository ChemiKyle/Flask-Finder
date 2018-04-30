import pandas as pd
import os
import sqlite3

__author__ = "R. Seaton Ullberg"


class LocationsMapper(object):

    def __init__(self):
        self._images_path = 'static/location_diagrams/'
        self.loc_names = self.get_location_names()
        self.img_files = self.get_image_files()
        self.autogen_config_file = 'location_fig.txt'
        self.map = None
        # auto generate a config template or read the existing one
        if not os.path.isfile(self.autogen_config_file):
            self.write_config_template()
        else:
            self.map = self.read_config_file()

    def write_config_template(self):
        with open(self.autogen_config_file, 'wb') as f:
            fill_string = "Detected Locations: {l}\n".format(f=self.img_files,
                                                             l=self.loc_names)
            fill_string += "\nProvide a comma separated list of corresponding location names for each image file below.\n"
            for fnames in self.img_files:
                fill_string += "\n{}:".format(fnames)
            f.write(bytes(fill_string, 'utf-8'))
            f.close()

    def read_config_file(self):
        _map = {}
        with open(self.autogen_config_file, 'rb') as f:
            for i, line in enumerate(f):
                if i > 3:
                    # relevant line to parse
                    split_line = line.split(bytes(':', 'utf-8'))
                    file_path = split_line[0]
                    location_names = split_line[1].split(bytes(',', 'utf-8'))
                    location_names = [li.decode('utf-8') for li in location_names]
                    location_names = [li.strip(' ') for li in location_names]
                    location_names = [li.strip('\n') for li in location_names]
                    try:
                        location_names.remove('')
                    except ValueError:
                        pass
                    _map[file_path.decode('utf-8')] = location_names
        return _map

    def get_location_names(self):
        conn = sqlite3.connect('db/inv.db', check_same_thread=False)
        c = conn.cursor()
        all_location_names = set()
        for table in ['equip', 'chem', 'stock']:
            loc_names = c.execute("SELECT Location FROM {}".format(table)).fetchall()
            loc_names = [locs[0] for locs in loc_names if locs[0] != '']
            for loc in loc_names:
                all_location_names.add(loc)
        conn.commit()
        conn.close()
        return all_location_names

    def get_image_files(self):
        img_list = [self._images_path+li for li in os.listdir(self._images_path) if li.endswith('.png') or li.endswith('.jpg')]
        return img_list

    def make_location_html(self):
        script_string = '<script>'
        script_string += '\nfunction showDiv(div_el,e) {\n\t'
        script_string += 'div_el.style.display = "block";\n\tdiv_el.style.left = e.clientX+"px";\n\tdiv_el.style.top = e.clientY+"px";\n}\n'
        script_string += '\nfunction hideDiv(element) {\n\t'
        script_string += 'element.style.display = "none";\n}\n'
        script_string += '</script>\n\n'

        style_string = '<style>\n\tdiv.location_div {'
        style_string += '\n\t\tz-index: 1;\n\t\tbackground-color: transparent;\n\t\t'
        style_string += 'top: 50px;\n\t\tleft: 765px;\n\t\tposition: absolute;\n\t\t'
        style_string += 'display: block;\n\t'
        style_string += '}\n</style>'
        for loc in self.loc_names:
            _url = None
            for img_file in self.img_files:
                if loc in self.map[img_file]:
                    _url = img_file
                    break
            img_string = '<img id="{id}" src="{src}" style="margin:auto; display:none; height:500px; width:800px; position:fixed;" />'.format(id=loc, src=_url)
            div_string = '\n<div class="location_div">\n\t{img}\n</div>'.format(img=img_string)
            style_string += div_string

        return script_string+style_string
