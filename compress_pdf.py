import PyPDF2
import io

def compress_pdf(input_pdf, output_pdf, target_size_bytes):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.compress_content_streams()  # Compress the content streams of the page

            # Check the size of the page
            temp_buffer = io.BytesIO()
            temp_writer = PyPDF2.PdfWriter(temp_buffer)
            temp_writer.add_page(page)
            temp_writer.write(temp_buffer)
            temp_size = temp_buffer.tell()

            # If the page size is within the target size, add it to the output PDF
            if temp_size <= target_size_bytes:
                pdf_writer.add_page(page)
            else:
                # You can further adjust compression settings or skip pages if needed
                print(f"Skipping page {page_num + 1} due to size ({temp_size} bytes)")

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

# Example usage
input_pdf = 'input.pdf'  # Input PDF file to compress
output_pdf = 'compressed_output.pdf'  # Output compressed PDF file
target_size_bytes = 1024 * 1024  # Target size in bytes (1 MB in this example)

compress_pdf(input_pdf, output_pdf, target_size_bytes)
