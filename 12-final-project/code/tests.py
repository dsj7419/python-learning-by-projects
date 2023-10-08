import unittest  # Importing the unittest module for testing
import os  # Importing os for file path operations
from data_processing import load_data  # Import the data loading function
from report_generation import create_visualizations, generate_report  # Import report generation functions

class TestDataProcessing(unittest.TestCase):
    def test_load_data(self):
        # TODO: Write tests for the load_data function.
        # HINT: Use self.assertIsNotNone to check that the function doesn't return None.
        # HINT: Use self.assertTrue to check that the returned data is non-empty.
        # HINT: Use self.assertIn to check that a key exists in the returned data.

        pass # Your code here
        
class TestReportGeneration(unittest.TestCase):
    def test_generate_report(self):
        # TODO: Write tests for the create_visualizations and generate_report functions.
        # HINT: Check that the visualization image file and report PDF are created successfully.
        # HINT: Use os.path.exists to check that a file exists.
        # HINT: Use os.remove to clean up files after testing to prevent clutter.
        
        pass # Your code here
        
        # Cleanup: Delete generated files to prevent clutter and save space.
        try:
            # Ensure critical files are not deleted by checking filenames before deletion.
            CRITICAL_FILES = ['new_student_data.csv']
            # Your cleanup code here
            
        except FileNotFoundError as e:
            # If a deletion fails, print a message to aid debugging.
            print(f"Error during cleanup: {str(e)}")

if __name__ == '__main__':
    unittest.main()
