def read_csv():
    import csv
    
    with open('example2.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
        

def write_csv():
    import csv
 
    myData = [["first_name", "second_name", "Grade"],
            ['Alex', 'Brian', 'A'],
            ['Tom', 'Smith', 'B']]
    
    myFile = open('example2.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
        
    print("Writing complete")

read_csv()