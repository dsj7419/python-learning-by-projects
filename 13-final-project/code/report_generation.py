import matplotlib.pyplot as plt  # For creating visualizations
from typing import List, Dict  # Type checking
from reportlab.lib.pagesizes import letter  # Page size for PDF
# Various components for creating PDFs
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet  # Styling for PDF
from reportlab.lib import colors  # Colors for PDF styling
import os  # File path operations

def create_visualizations(data: List[Dict[str, str]]) -> str:
    """
    Create a bar chart visualization showing the average scores in Mathematics, Science, and English.
    
    Parameters:
        data (List[Dict[str, str]]): A list of dictionaries containing student data.

    Returns:
        str: The file path of the saved visualization image.
    """
    try:
        # TODO: Extract scores and calculate averages for each subject.
        # HINT: Use list comprehensions and the sum and len functions.
        math_scores = None
        science_scores = None
        english_scores = None

        avg_math = None
        avg_science = None
        avg_english = None

        # TODO: Create a bar chart using matplotlib functions.
        # HINT: Use plt.bar() to create a bar chart and plt.savefig() to save the chart.
        subjects = ['Mathematics', 'Science', 'English']
        averages = [avg_math, avg_science, avg_english]

        # Your code here

        return None
    
    except Exception as e:
        print(f"Error creating visualization: {str(e)}")
        return None

def generate_report(data: List[Dict[str, str]], image_path: str) -> str:
    """
    Generate a PDF report which includes average scores visualization and detailed student scores.
    
    Parameters:
        data (List[Dict[str, str]]): A list of dictionaries containing student data.
        image_path (str): The file path of the visualization image.

    Returns:
        str: The file path of the generated PDF report.
    """
    try:
        # Define the path for the report PDF
        report_path = os.path.join("data", 'report.pdf')
        
        # TODO: Create the PDF document and add components to it.
        # HINT: Use SimpleDocTemplate, Paragraph, Image, and Table to construct the PDF.
        doc = None
        story = []
        styles = getSampleStyleSheet()

        # Your code here
        
        return None
    
    except Exception as e:
        print(f"Error generating report: {str(e)}")
        return None
