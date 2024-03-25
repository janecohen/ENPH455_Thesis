# saveData.py
# Date: February 2024
# Author: Jane Cohen

## Two functions for saving data collected b PicoScopes
## Import this module to a scope running script to use

import csv
import os
from datetime import datetime

def get_path(scope_num):
    # specify the parent folder path
    parent_folder_path = r'C:\Users\501ALabPC\Desktop\rotamak_JC-main'

    # check if the parent folder exists
    if not os.path.exists(parent_folder_path):
        os.makedirs(parent_folder_path)

    # get the current date
    current_datetime = datetime.now()
    year = current_datetime.year
    month = current_datetime.month
    day = current_datetime.day

    # create subfolder names based on year, month, and day
    year_folder = os.path.join(parent_folder_path, str(year))
    month_folder = os.path.join(year_folder, f"{month:02d}")  # Zero-padded month
    day_folder = os.path.join(month_folder, f"{day:02d}")  # Zero-padded day

    # create the subfolders if they don't exist
    for folder in [year_folder, month_folder, day_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # use 'day_folder' as the base path for files
    file_name = f"data_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}_Scope{scope_num}.csv"
    file_path = os.path.join(day_folder, file_name)

    return file_path

def save_to_csv(curr_dir, file_path, scope_num, time, channelA, channelB, flag_desktop, flag_gui):
    if(flag_desktop == True):
        # Combine the columns into rows
        rows = zip(time, channelA, channelB)
    
        # Write data to the CSV file
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header
            csv_writer.writerow(['Time (ns)', 'Voltage A (mV)', 'Voltage B (mV)'])

            # Write data rows
            for i, row in enumerate(rows):
                # Check if the index is a multiple of 100 (starting from 0)
                if i % 100 == 0:
                    # Write the row to the CSV
                    csv_writer.writerow(row)

            print(f"\n Data saved to: {file_path}")

    if(flag_gui == True):
        path = f"{curr_dir}GUI/collected_data/Scope {scope_num}/Channel A/data.csv"
        # Combine the columns into rows
        rows = zip(time, channelA)

        # Write data to the CSV file
        with open(path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header
            csv_writer.writerow(['Time (ns)', 'Voltage (mV)'])

            # Write data rows
            for i, row in enumerate(rows):
                # Check if the index is a multiple of 100 (starting from 0)
                if i % 100 == 0:
                    # Write the row to the CSV
                    csv_writer.writerow(row)

            print(f"\n Data saved to: {path}")

        path = f"{curr_dir}GUI/collected_data/Scope {scope_num}/Channel B/data.csv"
        # Combine the columns into rows
        rows = zip(time, channelB)

        # Write data to the CSV file
        with open(path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header
            csv_writer.writerow(['Time (ns)', 'Voltage (mV)'])

            # Write data rows
            for i, row in enumerate(rows):
                # Check if the index is a multiple of 100 (starting from 0)
                if i % 100 == 0:
                    # Write the row to the CSV
                    csv_writer.writerow(row)
                    
            print(f"\n Data saved to: {path}")

    
