import csv  

# reading a file
with open('supportvolscores.csv') as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# writing a file
with open('file.txt', 'w') as f:
    f.write('Hi I am a file!')
    f.close()
