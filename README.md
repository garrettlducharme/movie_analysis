# movie_analysis
A project for providing insight into which kinds of movies perform well in terms of viewer satisfaction and profitability on both a domestic and worldwide scale in the past 10 years

## Project Members

- Joseph Cohen
- Garrett DuCharme

## Goals

The goal of this project is to determine which kinds of movies Microsoft should be producing in order to maximize viewer satisfation as well as profits. In order to determine which movies to produce, we will first look at viewer ratings based on genre. For genres that do well, we will use the ratios between both domestic and international profits with the production cost as a metric to determine which movies to focus on to maximize profits. All of this analysis will be focused on movies produced no earlier than 2010 in order to best reflect what the market currently demands.

## Responsibilities
    
- Garrett's responsibilities
    - Determining intitial questions of interest
    - Markdown for this readme file
    - Consolidating functions into the data_cleaner.py module
    - Adding the movie_data_plotter.py module for larger plotting functions
    - Markdown for the technical notebook
    - Creating summary tables
    
    
- Joseph's responsibilities
    - Finding corresponding genre names for genre IDs in tmdb.movies.csv
    - Creating a dictionary to map genre ID to genre name
    - Doing scratch work for the data cleaning functions
    - Markdown for the nontechnical notebook
    - Consolidating work into the presentation
    
## Summary of Files

### README.md

This readme file

### data_cleaner.py

Contains functions that clean and merge the pandas DataFrames

### movie_data_plotter.py

Contains functions for creating the horizontal bar plots in the technical notebook

### technical_notebook.ipynb

Notebook with markdown and technical details about the data cleaning and analysis

### non_technical_notebook.ipynb

Notebook with plots and tables that provide a narrative of the findings as opposed to a technical writeup

### img

Folder containing images for the nontechnical notebook

### data

Directory containing the datasets, including those that were considered but not used in the analysis

