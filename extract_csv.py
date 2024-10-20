import csv

# Extract the content from a CSV file
def extract_csv(self, csv_file):
    with open(csv_file, newline='') as csvfile:
        read_csv = csv.DictReader(csvfile)
        csv_extract = [row for row in read_csv]
        
        return csv_extract

# Create a single instance of FileReader
file_reader = FileReader()

# Print the content of the CSV file
csv_extract = file_reader.extract_csv('')
print(csv_extract)