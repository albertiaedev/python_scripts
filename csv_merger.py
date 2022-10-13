import csv

def merge_csv(csv_list, output_path):

    field_names = []
    for file in csv_list:
        with open(file, 'r') as input_csv:
            fn = csv.DictReader(input_csv).field_names
            field_names.extend(x for x in fn if x not in field_names)

    with open(output_path, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, field_names=field_names)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)
