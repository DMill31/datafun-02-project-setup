"""
Module: miller_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Daniel Miller
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
import pathlib
from time import sleep

# Import local modules
import utils_miller 

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    for year in range(start_year, end_year+1):
        # Create a folder path for the year
        year_path = data_path.joinpath(str(year))

        # Create the year folder if it doesn't exist, otherwise do nothing
        year_path.mkdir(exist_ok=True)

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool, remove_spaces: bool) -> None:
    '''
    Create folders from a list of names.
    
    Arguments:
    folder_list -- A list of folder names to create.
    to_lowercase -- A boolean flag to convert names to lowercase.
    remove_spaces -- A boolean flag to remove spaces from names.
    '''

    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, to_lowercase={to_lowercase}, and remove_spaces={remove_spaces}")

    for name in folder_list:
        # Convert the name to lowercase if the flag is set
        if to_lowercase:
            name = name.lower()
        #Remove spaces from the name if the flag is set
        if remove_spaces:
            name = name.replace(" ", "")

        # Create a folder path for the name
        name_path = data_path.joinpath(name)

        # Create the name folder if it doesn't exist, otherwise do nothing
        name_path.mkdir(exist_ok=True)


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create prefixed folders by combining a prefix with a list of names.
    
    Arguments:
    folder_list -- A list of folder names.
    prefix -- A string to add to the beginning of each folder name.
    '''
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")

    for name in folder_list:
        # Create a folder path for the name
        name_path = data_path.joinpath(prefix + name)

        # Create the name folder if it doesn't exist, otherwise do nothing
        name_path.mkdir(exist_ok=True)

  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically at a given interval.
    
    Arguments:
    duration_seconds -- The time to wait between creating folders.
    '''
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")

    folder_num = 3
    #Number of folders to create

    while folder_num > 0:
        # Create a folder path for the folder number
        folder_path = data_path.joinpath(f"folder_{folder_num}")

        # Create the folder if it doesn't exist, otherwise do nothing
        folder_path.mkdir(exist_ok=True)

        # Decrement the folder number
        folder_num -= 1

        # Wait for the duration
        sleep(duration_seconds)


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_miller.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names,to_lowercase=False, remove_spaces=False)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)


    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()