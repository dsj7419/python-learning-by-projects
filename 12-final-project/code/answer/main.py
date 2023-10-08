import os
import data_processing
import report_generation
import email_system

def main():
    """
    Main function to orchestrate the loading, processing, and mailing of student data.
    """
    try:
        # Display a welcome message to the user.
        print("Welcome to the Automated Report Generation and Mailing System!")
        
        # Ensure the data directory exists to store our generated files.
        if not os.path.exists("data"):
            os.makedirs("data")  # If not, create it.
        
        # Specify the path to the data and attempt to load it.
        data_path = "new_student_data.csv"
        data = data_processing.load_data(data_path)

        
        # Check whether data was successfully loaded.
        if data is None:
            print(f"Data loading failed. Please ensure the data file is located at {data_path}")
            return
        
        # Gather email credentials and recipient information.
        print("\nLet's set up your email...")
        email, password = email_system.get_email_credentials()
        recipient_email = input("Enter the recipient's email address: ")
        
        # Generate and dispatch the report.
        print("\nGenerating and sending the report...")
        
        # Create a visualization for the report.
        image_path = report_generation.create_visualizations(data)
        if image_path is None:
            print("Visualization creation failed.")
            return

        # Generate the report PDF.
        report_path = report_generation.generate_report(data, image_path)
        if report_path is None:
            print("Report generation failed.")
            return
        
        # Send the report via email.
        email_subject = "Student Performance Report"
        email_body = "Find attached the Student Performance Report."
        email_sent = email_system.send_email(email, password, email_subject, email_body, recipient_email, report_path)
        
        # Inform the user about the email status.
        if email_sent:
            print("Report sent successfully!")
        else:
            print("Report could not be sent via email.")
        
        # Indicate that the process is complete.
        print("\nProcess completed!")

    except Exception as e:
        # Handle any unexpected errors and display a message to the user.
        print(f"An error occurred: {str(e)}")

# Ensure the main function is only run when this script is executed directly.
if __name__ == "__main__":
    main()