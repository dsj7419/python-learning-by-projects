import os  # For file path operations
import csv  # To read CSV data
from typing import List, Dict  # For type hinting

def load_data(file_name: str) -> List[Dict[str, str]]:
    """
    Load student data from a CSV file.

    Parameters:
        file_name (str): The name of the CSV file located in the "data" directory.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the student data from the CSV file, or
                              None if an error occurs during data loading.
                              
    Note: 
        Each dictionary represents a student's data with keys as the data headers and values as the student scores.
    """
    # TODO: Construct the full file path by combining the directory name with the file name.
    # HINT: Use os.path.join to concatenate the directory and filename.
    file_path = None
    
    # Display a message indicating the file path being loaded
    print(f"Trying to load data from: {file_path}")
    
    try:
        # TODO: Open the file and read the data into a list of dictionaries.
        # HINT: Use with statement to open the file and csv.DictReader to read the data.
        data = None
        
        return data
    
    # Handle specific and general errors during data loading
    except FileNotFoundError:
        print(f"No file found at {file_path}. Please ensure the file path is correct.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
