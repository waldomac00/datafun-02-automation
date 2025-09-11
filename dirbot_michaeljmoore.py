"""
File: dirbot_michaeljmoore.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Hint: See the Textbook, Skill Drills, and GUIDES for code snippets to help complete this module.

Author: Michael J Moore

"""

#####################################
# Import Modules at the Top
#####################################

# Import from the Python Standard library
import pathlib
import sys   
import time  # Needed For Function 4 below   

# Import packages from requirements.txt
import loguru   

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
import utils_michaeljmoore

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare global variables
#####################################

# Create a project path object for the root directory of the project.
ROOT_DIR = pathlib.Path.cwd()

REGIONS = [
    "North America", 
    "South America", 
    "Europe", 
    "Asia", 
    "Africa", 
    "Oceania", 
    "Middle East"
]

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., years).
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
    # Log function name and parameters
    logger.info("FUNCTION: create_folders_for_range()")
    logger.info(f"PARAMETERS: start_year = {start_year}, end_year = {end_year}")

    # Loop through the years from start_year to end_year (inclusive)
    # For each year, create a folder using ROOT_DIR / str(year)
    # Log a message each time a folder is created
    # Use .mkdir(exist_ok=True) so the program doesn't crash if the folder already exists

    for year in range(start_year, end_year + 1):
        year_path = ROOT_DIR / str(year)
        year_path.mkdir(exist_ok=True)
        (year_path / ".gitkeep").touch(exist_ok=True)  # Add to create a .gitkeep file in each folder
        logger.info(f"Created folder: {year_path}")

    # Example starter structure:
    # for year in range(start_year, end_year + 1):
    #     year_path = ROOT_DIR / str(year)
    #     year_path.mkdir(exist_ok=True)
    #     logger.info(f"Created folder: {year_path}")


  
#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################

def create_folders_from_list(folder_list: list) -> None:
    '''
    Create folders based on a list of folder names.
    
    Arguments:
    folder_list -- A list of strings representing folder names.
    '''
    logger.info("FUNCTION: create_folders_from_list()")
    logger.info(f"PARAMETER: folder_list = {folder_list}")

    # Loop through the list of folder names
    # For each name, create a folder using ROOT_DIR / name
    # Log a message each time a folder is created
    # Ensure folder names are lower case and have no spaces

    for name in folder_list:
        folder_name = str(name)
        folder_name = folder_name.replace(" ", "_").lower()
        name_path = ROOT_DIR / folder_name
        name_path.mkdir(exist_ok=True)
        (name_path / ".gitkeep").touch(exist_ok=True)  # Add to create a .gitkeep file in each folder
        logger.info(f"Created folder: {name_path}")


    pass


  
#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################

def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each item in a list 
    using a concise form of a for loop called a list comprehension.

    Arguments:
    folder_list -- A list of strings (e.g., ['csv', 'excel']).
    prefix -- A string to prefix each name (e.g., 'output-').
    '''

    logger.info("FUNCTION: create_prefixed_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, prefix = {prefix}")

    # Create a list of prefixed folder names using list comprehension
    # Iterate over the prefixed names, create each folder, and log the action

    for name in folder_list:
        prefix_name_path = ROOT_DIR / str(prefix + name)
        prefix_name_path.mkdir(exist_ok=True)
        (prefix_name_path / ".gitkeep").touch(exist_ok=True)  # Add to create a .gitkeep file in each folder
        logger.info(f"Created folder: {prefix_name_path}")



  

#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically over time.

    Arguments:
    duration_seconds -- The number of seconds to wait between folder creations.
    '''    
    logger.info("FUNCTION: create_folders_periodically()")
    logger.info(f"PARAMETER: duration_seconds = {duration_seconds}")

    # Create folders for each math class, waiting between each creation.
    # Each folder is named with a count and the class name (e.g., "1_algebra").
    # Wait for the specified duration before creating the next folder.

    math_classes =  ['algebra', 'geometry', 'calculus', 'statistics', 'trigonometry']
    count = 1
    for class_name in math_classes:
        math_folder = f"{count}_{class_name}"
        folder_path = ROOT_DIR / math_folder
        folder_path.mkdir(exist_ok=True)
        (folder_path / ".gitkeep").touch(exist_ok=True)  # Add to create a .gitkeep file in each folder
        logger.info(f"Created folder: {folder_path}")
        count += 1
        time.sleep(duration_seconds)
    
     
    pass


#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################

def create_standardized_folders(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of names with options to standardize names.

    Arguments:
    folder_list -- A list of strings representing folder names.
    to_lowercase -- If True, convert names to lowercase.
    remove_spaces -- If True, remove spaces from names.
    '''

    logger.info("FUNCTION: create_standardized_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, to_lowercase = {to_lowercase}, remove_spaces = {remove_spaces}")

    # Example folder names using taco
    
    taco_types = ['Al Pastor', 'Carne Asada', 'Fish', 'Carnitas']

    # Loop through the list of folder names
    # For each name, apply transformations based on parameters
    # Create a folder using ROOT_DIR / transformed_name
    # Log a message each time a folder is created
    # Ensure folder names are lower case and/or have no spaces based on parameters
    # Example folder names to create

    for tacos in taco_types:
        taco_folder = str("Taco " + tacos)
        if to_lowercase:
           taco_folder = taco_folder.lower()
        if remove_spaces:
            taco_folder = taco_folder.replace(" ", "_")
        taco_path = ROOT_DIR / taco_folder
        taco_path.mkdir(exist_ok=True)
        (taco_path / ".gitkeep").touch(exist_ok=True)  # Add to create a .gitkeep file in each folder
        logger.info(f"Created folder: {taco_path}")
        

    pass
  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''
#
    logger.info("#####################################")
    logger.info("# Starting execution of main()")
    logger.info("#####################################\n")

    #Change this to use your module and your get_byline() function instead
    logger.info(f"Byline: {utils_michaeljmoore.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using list comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'output-'
    create_prefixed_folders_using_list_comprehension(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call function 5 to create standardized folders, no spaces, lowercase
    create_standardized_folders(REGIONS, to_lowercase=True, remove_spaces=True)

    logger.info("\n#####################################")
    logger.info("# Completed execution of main()")
    logger.info("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()