# PurpleAir and AADT Analysis - GEOG 5563 Final Project

This repository contains Python code used in our final GIS analysis project for GEOG 5563.

## Contributors
- Mahsa Abdolyashtiyani  
- Martha Denton  
- Isabel Eguizabal

## Description
We used PurpleAir sensor data and AADT (Average Annual Daily Traffic) data to assess vehicle-related air pollution in the Twin Cities Metro Area. The project involved:

- Retrieving and filtering PM2.5 data from PurpleAir API
- Calculating median PM2.5 for each sensor
- Removing extreme values above 500 µg/m³
- Spatial interpolation using Kriging in ArcGIS Pro
- Zonal statistics to compare PM2.5 with census data

## Files
- colab_data_download.py: Script used in Google Colab for downloading PurpleAir data
- calculate_median_pm25.py: Script for cleaning and calculating median PM2.5 values
- visualize_distribution.py: Histogram of sensor medians

## Source
- PurpleAir API: (https://www2.purpleair.com)
- AADT Data: Minnesota DOT

## Note
See the final project report and slides for detailed analysis and results.
