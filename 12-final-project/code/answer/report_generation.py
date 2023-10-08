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
        # Extract scores and calculate averages
        math_scores = [int(student['Mathematics']) for student in data]
        science_scores = [int(student['Science']) for student in data]
        english_scores = [int(student['English']) for student in data]

        avg_math = sum(math_scores) / len(math_scores)
        avg_science = sum(science_scores) / len(science_scores)
        avg_english = sum(english_scores) / len(english_scores)

        # Define subjects and their corresponding averages
        subjects = ['Mathematics', 'Science', 'English']
        averages = [avg_math, avg_science, avg_english]

        # Create a bar chart
        plt.figure(figsize=(8, 6))
        plt.bar(subjects, averages, color=['blue', 'green', 'red'])
        plt.ylim(0, 100)
        plt.ylabel('Average Score')
        plt.title('Average Scores in Different Subjects')

        # Save the visualization as a .png file
        image_path = os.path.join("data", 'average_scores.png')
        plt.savefig(image_path)
        plt.close()

        return image_path
    
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
        
        # Create the PDF document
        doc = SimpleDocTemplate(report_path, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()

        # Add components to the PDF
        story.append(Paragraph("Student Performance Report", styles['Title']))
        story.append(Paragraph("Average Scores", styles['Heading2']))
        
        # Add the bar chart image if available
        if image_path is not None:
            story.append(Image(image_path, width=270, height=200))
        else:
            story.append(Paragraph("Error generating visualization.", styles['BodyText']))
        
        story.append(Paragraph("Detailed Scores", styles['Heading2']))
        
        # Create a table data list
        table_data = [["Name", "Mathematics", "Science", "English"]]  # Header row
        
        # Add student data to the table
        for student in data:
            table_data.append([student['Name'], student['Mathematics'], student['Science'], student['English']])
        
        # Create and style the table
        scores_table = Table(table_data)
        table_style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 1), (-1, -1), 1, colors.black)
        ])
        scores_table.setStyle(table_style)
        
        # Add the table to the story
        story.append(scores_table)
        
        # Build the PDF document
        doc.build(story)

        return report_path
    
    except Exception as e:
        print(f"Error generating report: {str(e)}")
        return None
