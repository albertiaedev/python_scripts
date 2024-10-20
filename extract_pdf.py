import PyPDF2

# Extract the content from a PDF file
def extract_pdf(self, pdf_file: str):
    with open(pdf_file, 'rb') as pdf:
        read_pdf = PyPDF2.PdfReader(pdf)
        pdf_extract = []

        for page in read_pdf.pages:
            content = page.extract_text()
            pdf_extract.append(content)

        return pdf_extract

# Create a single instance of FileReader
file_reader = FileReader()

# Print the content of the PDF file
pdf_extract = file_reader.extract_pdf('')
for text in pdf_extract:
    print(text)