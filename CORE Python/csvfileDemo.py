import csv

def handle_values(input_file, default_value):
    with open(input_file, mode='r') as infile:
        reader = csv.reader(infile)
        rows=[row for row in reader]
        updated_rows=[]
        for row in rows:
            updated_row=[value if value !=' 'else default_value for value in row]       
            updated_rows.append(updated_row)
            print(updated_row)


    
handle_values('csvdemo.csv','unknown')