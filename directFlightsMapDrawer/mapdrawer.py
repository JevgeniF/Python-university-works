"""Script for Tallinn direct filght connections drawing."""

import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def directFlights():
    """
    Generate and save map with direct fligts from/to Tallinn, Estonia.

    Uses two files "directfligts.csv" and "airports.dat" to get datframe with
    IATA, Longitude and Latitude of required airports. Using this dataframe,
    the script generates map and draws direct flight connections.

    Returns
    -------
    None.

    """
    # Opening files with pandas and generate requred mainframes:
    direct = pd.read_csv("directflights.csv", sep=';', header=0)[["IATA"]]
    airports = pd.read_csv("airports.dat", sep=',', header=0,
                           usecols=[4, 6, 7])
    arrivals = airports.loc[airports["IATA"].isin(direct["IATA"])]

    # Generating world map by matphlotlib and cartopy.
    world = plt.axes(projection=ccrs.PlateCarree())
    world.set_extent([-10, 45, 34, 65], ccrs.PlateCarree())
    world.stock_img()
    world.coastlines()

    # Plotting points and names for airports and connecting lines.
    for index, row in arrivals.iterrows():
        if 'TLL' in row['IATA']:
            world.plot(row["Longitude"], row["Latitude"], marker='o',
                       color='blue')
            world.text(row["Longitude"] + 0.5, row["Latitude"] - 0.5,
                       row['IATA'], size=7, color='blue')
        else:
            world.plot(row["Longitude"], row["Latitude"], marker='o',
                       markersize=5, color='red')
            world.text(row["Longitude"] + 0.5, row["Latitude"] - 0.5,
                       row['IATA'], size=7, color='red')
        world.plot([24.832799911499997, row['Longitude']],
                   [59.41329956049999, row['Latitude']], color='blue',
                   transform=ccrs.Geodetic())

    # Preparing outcome: wolrd.png file with DPI 250, name of map.
    plt.title("Direct Flights from Tallinn, Estonia")
    plt.savefig("world.png", dpi=250)
    plt.show()


directFlights()
