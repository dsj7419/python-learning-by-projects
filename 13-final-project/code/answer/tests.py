import unittest  # Importing the unittest module for testing
import os  # Importing os for file path operations
from data_processing import load_data  # Import the data loading function
from report_generation import create_visualizations, generate_report  # Import report generation functions

# Define a class to test data processing functions.
class TestDataProcessing(unittest.TestCase):
    # Test the functionality of loading data from a file.
    def test_load_data(self):
        # Attempt to load data from the provided CSV file.
        data = load_data('new_student_data.csv')
        
        # Check that the data is not None, indicating it was loaded successfully.
        # Also check that it contains some data by checking its length.
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)
        
        # Check that "Name" is a key in the data, ensuring the structure is as expected.
        self.assertIn("Name", data[0].keys())
        
# Define a class to test report generation functions.
class TestReportGeneration(unittest.TestCase):
    # Test the functionality of generating a report.
    def test_generate_report(self):
        # Load data to be used for generating the report.
        data = load_data('new_student_data.csv')
        
        # Create a visualization based on the loaded data.
        image_path = create_visualizations(data)
        
        # Generate a report using the data and visualization, saving the path.
        report_path = generate_report(data, image_path)
        
        # Check that the report file exists, indicating it was created successfully.
        self.assertTrue(os.path.exists(report_path))
        
        # Define critical files that should not be deleted during cleanup.
        CRITICAL_FILES = ['new_student_data.csv']

        # Cleanup: Delete generated files to prevent clutter and save space.
        try:
            # Ensure critical files are not deleted by checking filenames before deletion.
            if os.path.basename(report_path) not in CRITICAL_FILES:
                os.remove(report_path)
            if os.path.basename(image_path) not in CRITICAL_FILES:
                os.remove(image_path)
        except FileNotFoundError as e:
            # If a deletion fails, print a message to aid debugging.
            print(f"Error during cleanup: {str(e)}")

# Execute tests when the script is run directly.
if __name__ == '__main__':
    unittest.main()