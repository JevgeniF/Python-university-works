# Script for drawing of Direct Flight connections with Tallinn Airport.

The script generates and saves map with direct fligts from/to Tallinn, Estonia.

It uses 2 files for creation of dataframes.
1. "direcflights.csv" used to get dataframe "direct" with IATA codes of airports with direct connection from/to Tallinn, Estonia
2. "airports.dat" is the database of world airports, sused to get dataframe airports wiht IATA codes, Longitude and Latitude of airports.
3. "arrivals" dataframe generated as filter for airports database, to get only data of airports with direct connections.

The map generated with cartopy and mathplotlib. We use only part of world required to show connections with Tallinn.

Points, names, lines plotted with loop via arrivals dataframe. Tallinn (TLL) point dedicated and marked by blue color.

Script shows map on screen and saves it as "world.png" file with resolution 250 DPI.


Created as Homework 3 for ICS0019 course.
Created by Jevgeni Fenko
jefenk@taltech.ee
200810IADB