from generate_report import *
from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.transform import jitter

df = unroll_dt(fetch_data())
x = df.Weekday
y = df.Hour + df.Minute / 60.

# Causes weird offset
DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

p = figure(title="Searches by Weekday and Time", match_aspect=True,
           tools="wheel_zoom,reset", background_fill_color='#440154',
           x_range=(0, 6),y_range=(24, 0))
p.grid.visible = False

r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

#Jitter returns valueError
p.circle(x=x, y=y,
                color="white", size=2, alpha = 0.8)

hover = HoverTool(tooltips=[("count", "@c")],
                                  mode="mouse", point_policy="follow_mouse", renderers=[r])

p.add_tools(hover)

# output_file("hexbin.html")

# p.y_range = Range1d(y.max(),y.min())

show(p)
