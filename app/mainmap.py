"""The following is dedicated to the main map with historical air quality data.

The main item is the main_map function that returns the corresponding map object.
"""
# ------------------------------------------------------------------------------
# Imports

from pathlib import Path

import pandas as pd

import plotly.express as px



# reading the stations locations .csv file and storing it
data_path = Path(__file__).parent.parent.joinpath('data', 'raw', 'stations_locations.csv')
stations_locations = pd.read_csv(data_path)



# this function returns a fig object (px.scatter) with stations locations data
def build_main_map():
    fig = px.scatter_mapbox(stations_locations, lat="latitude", lon="longitude", hover_name="station_id", hover_data=["latitude", "longitude"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=600)
    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "sourceattribution": "United States Geological Survey",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
          ])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig
