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
    # Combine the directory name with the file name to get the full file path
    file_path = os.path.join("data", file_name)

    # Display a message indicating the file path being loaded
    print(f"Trying to load data from: {file_path}")
    
    try:
        # Open the file and read the data into a list of dictionaries
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Use DictReader to directly read header:data into a dictionary
            data = [row for row in reader]  # List comprehension to convert the CSV data into a list of dictionaries
        return data
    
    # Handle specific and general errors during data loading
    except FileNotFoundError:
        print(f"No file found at {file_path}. Please ensure the file path is correct.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
