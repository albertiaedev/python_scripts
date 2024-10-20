import openpyxl

# Extract the content from a XLSX file
    def extract_xlsx(self, xlsx_file):
        workbook = openpyxl.load_workbook(xlsx_file)
        sheet = workbook.active
        xlsx_extract = []

        for row in sheet.iter_rows(values_only=True):
            xlsx_extract.append(list(row))

        return xlsx_extract

# Create a single instance of FileReader
file_reader = FileReader()

# Print the content of the XLSX file
xlsx_extract = file_reader.extract_xlsx('')
print(xlsx_extract)