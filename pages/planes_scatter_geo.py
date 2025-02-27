import dash
from dash import html, dcc

from utils.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app connects between a dropdown and two graphs: scatter_geo (also called Bubble map) and scatter_mapbox",
)

filename = __name__.split("pages.")[1]

# any notes will be displayed below the code-and-show page in a dcc.Markdown component
notes = """

Dash docs:  

- [Dropdown component](https://dash.plotly.com/dash-core-components/dropdown)

#### Plotly Documentation:  

- [Scatter Mapbox](https://plotly.com/python/mapbox-layers/) 
- [Scatter Geo](https://plotly.com/python/bubble-maps/) 
- [Map Configuration: Mapbox Maps vs Geo Maps ](https://plotly.com/python/map-configuration/)

#### Contributed by:
This example app was contributed by [someshfengde](https://github.com/someshfengde)

"""

layout = html.Div([example_app(filename), dcc.Markdown(notes, className="m-4")])
