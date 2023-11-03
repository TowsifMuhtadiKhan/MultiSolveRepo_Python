# Before run this code please install 'pip install PyPDF2'

from PyPDF2 import PdfMerger

def merge_pdfs(input_pdfs, output_pdf):
    merger = PdfMerger()

    for pdf_file in input_pdfs:
        merger.append(pdf_file)

    merger.write(output_pdf)
    merger.close()

# Example usage
input_pdfs = ['file1.pdf', 'file2.pdf']  # List of PDF files to merge, replace name according to your file(s)name
output_pdf = 'merged_output.pdf'  # Output file name, change this according to your requirement

merge_pdfs(input_pdfs, output_pdf)