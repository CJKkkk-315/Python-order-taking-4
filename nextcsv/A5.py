import csv

# Define the input and output file names
input_file = "NameData.csv"
output_file = "NameSelect.csv"

# Initialize the new list
datselect = []

# Open the input file and read the data
with open(input_file, "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Save the header row
    for row in reader:
        age = row[2]
        if int(age) < 40:
            datselect.append(row)

# Open the output file and write the data
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)  # Write the header row
    writer.writerows(datselect)  # Write the selected data

print("Selected names have been written to", output_file)