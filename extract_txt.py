class FileReader:
               
    # Extract the content from a TXT file
    def extract_txt(self, txt_file: str):
        with open(txt_file, 'r') as file:
            read_txt = file.readlines()
            txt_extract = [line.strip() for line in read_txt]

            return txt_extract

# Create a single instance of FileReader
file_reader = FileReader()

# Print the content of the TXT file
txt_extract = file_reader.extract_txt('')
print(txt_extract)