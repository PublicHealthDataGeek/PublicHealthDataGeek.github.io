# Script for interactive maps for TDS assignment
# Student: 940065422

# PLEASE NOTE - this code runs best if you run each chunk by itself due to the volume of data being
# downloaded

# Install relevent libraries
library(tidyverse)
library(sf)
library(osmdata)
library(mapview)
library(geojsonsf)

# Get boundary box for Greater London
GLxy = getbb("greater london")

# Obtain TFL CycleSuperhighway and Quietways data
urlCSH = "https://cycling.data.tfl.gov.uk/CycleRoutes/Cycle_Superhighways.json"
TFL_CSH = geojson_sf(urlCSH)

urlQuiet = "https://cycling.data.tfl.gov.uk/CycleRoutes/Quietways.json"
TFL_Quiet = geojson_sf(urlQuiet)

# Obtain OSM CycleSuperhighway and Quietways data 
OSM_CSH = opq(bbox = GLxy) %>%
  add_osm_feature(key = "cycle_network", value = "UK:London Cycleways") %>%
  osmdata_sf()

OSM_Quiet = opq(bbox = GLxy) %>%
  add_osm_feature(key = "cycle_network", value = "UK:London Quietways") %>%
  osmdata_sf()


# Create Interactive maps - works best if run individually ----------------


# Map 1 - displays Cyclesuperhighways data
m1 = mapview(TFL_CSH$geometry, color = 'red')
m2 = mapview(OSM_CSH$osm_lines, color = 'blue', legend = FALSE)
sync(m1, m2)

# Map 2 - displays Quietways data
m3 = mapview(TFL_Quiet$geometry, color = 'red')
m4 = mapview(OSM_Quiet$osm_line, color = 'blue', legend = FALSE)
sync(m3,m4)

# Map 3 - compares OSM Quietways with TFL minihollands, central london grid and quietways
urlMH = "https://cycling.data.tfl.gov.uk/CycleRoutes/Mini_Hollands.json"
TFL_MH = geojson_sf(urlMH)
urlCLG = "https://cycling.data.tfl.gov.uk/CycleRoutes/Central_London_Grid.json"
TFL_CLG = geojson_sf(urlCLG)
m5 = mapview(TFL_MH$geometry, color = 'orange')
m6 = mapview(TFL_CLG$geometry, color = 'green')
sync(list(m4,m6,m3,m5), ncol = 4)

# End