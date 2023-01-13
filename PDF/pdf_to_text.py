# This script converts a PDF file to text by using the PyPDF2 library. 
# The script opens the PDF file in read-binary mode, creates a PDF object using the PdfReader class, 
# and iterates over every page in the PDF. For each page, it extracts the text using the extract_text 
# method and prints it to the console. 
import PyPDF2

# Open the PDF file in read-binary mode
with open('PrepSharp_Co-op_Flyer.pdf', 'rb') as file:

    # Create a PDF object
    pdf = PyPDF2.PdfReader(file)

    # Iterate over every page
    for page in range(len(pdf.pages)):
        # Extract the text from the page
        text = pdf.pages[page].extract_text()

        # Print the text
        print(text)
