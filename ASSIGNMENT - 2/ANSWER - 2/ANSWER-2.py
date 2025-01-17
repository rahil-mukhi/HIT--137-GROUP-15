# Importing required libraries
# Here we are using pandas because it's best for working with tabular data
import os
import pandas as pd

all_df = []

for file in os.listdir('temperature_data'):  # Reading the csv files
    file_path = os.path.join('temperature_data', file)
    all_df.append(pd.read_csv(file_path))

all_df = pd.concat(all_df)

seasons = {
    'Spring': ['September', 'October', 'November'],
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August']
}


def calculate_seasonal_averages(df, seasons, output_file):  # Creating Function for calculating average for all seasons
    seasonal_avg = {}
    for season, months in seasons.items():
        seasonal_avg[season] = df[months].mean(axis=1)  # Mean temperature for the season
    for season, avg_temp in seasonal_avg.items():
        df[season] = avg_temp  # Add seasonal averages to DataFrame

    # Writing average temperatures for each season across all stations to a file.
    seasonal_avg_across_all_years = {season: df[season].mean() for season in seasons.keys()}
    with open(output_file, 'w') as f:
        for season, avg_temp in seasonal_avg_across_all_years.items():
            f.write(f" Average Temperature in {season} : {avg_temp:.2f} Celsius\n")
    print(f"Seasonal averages for all data written to {output_file}")

