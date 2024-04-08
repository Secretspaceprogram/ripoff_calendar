import sys
import os
from PyPDF2 import PdfMerger

def numerical_sort(value):
    # Extract numeric part of the filename
    return int(''.join(filter(str.isdigit, value)))

def combine_pdfs(input_dir, output_file):
    merger = PdfMerger()

    # Get a sorted list of PDF files in the directory
    pdf_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".pdf")], key=numerical_sort)

    # Iterate through sorted PDF files
    for file in pdf_files:
        file_path = os.path.join(input_dir, file)
        # Append each PDF to the merger object
        merger.append(file_path)

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as output:
        merger.write(output)

    merger.close()

# Example usage:
input_directory = sys.argv[1]  # Replace with your directory containing PDFs
output_pdf = sys.argv[2]  # Output file name
combine_pdfs(input_directory, output_pdf)
print("PDFs combined successfully into", output_pdf)
