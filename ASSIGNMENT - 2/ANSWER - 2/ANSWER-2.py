# GROUP NAME : CAS/DAN GROUP-15
# GROUP MEMBERS: 385218 RAHIL MUKHI
#                374427 RENISH VEKARIYA
#                384646 RUHINA RAJABALI
#                383635 RUSHABHKUMAR SAVAJ

# Importing required libraries
# Here we are using pandas because it's best for working with tabular data
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


def calculate_largest_temperature_range(df, output_file):  # Calculating temperature range for each station
    df['Temp_Range'] = df.iloc[:, 4:16].max(axis=1) - df.iloc[:, 4:16].min(axis=1)
    # Writing the station with the largest temperature range to a file.
    largest_temp_range_station = df.loc[df['Temp_Range'] == df['Temp_Range'].max()]
    with open(output_file, 'w') as f:
        f.write("Station with largest temperature range in Australia: ")
        for _, row in largest_temp_range_station.iterrows():
            f.write(f"{row['STATION_NAME']} (Temperature Range: {row['Temp_Range']:.2f} Celsius)\n")
    print(f"Largest temperature range station written to {output_file}")


def warmest_and_coldest_temperature(df, output_file):
    # Calculating maximum and minimum temperatures for each station
    df['Max_Temperature'] = df.iloc[:, 4:16].max(axis=1)
    df['Min_Temperature'] = df.iloc[:, 4:16].min(axis=1)
    # Writing warmest and coolest stations to a file
    warmest_station = df.loc[df['Max_Temperature'] == df['Max_Temperature'].max()]
    coolest_station = df.loc[df['Min_Temperature'] == df['Min_Temperature'].min()]
    with open(output_file, 'w') as f:
        f.write("Warmest Station in Australia: ")
        for _, row in warmest_station.iterrows():
            f.write(f"{row['STATION_NAME']} (Max Temperature: {row['Max_Temperature']:.2f} Celsius)\n")
        f.write("\nCoolest Station in Australia: ")
        for _, row in coolest_station.iterrows():
            f.write(f"{row['STATION_NAME']} (Min Temperature: {row['Min_Temperature']:.2f} Celsius)\n")
    print(f"Warmest and coolest stations are written to {output_file}")


# Calling all the functions
calculate_seasonal_averages(all_df, seasons, 'average_temp.txt')

calculate_largest_temperature_range(all_df, 'largest_temp_range_station.txt')

warmest_and_coldest_temperature(all_df, 'warmest_and_coldest_station.txt')
