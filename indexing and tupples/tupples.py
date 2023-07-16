filenames = ["1. raw data.txt","2. reports.txt","3. presentations.txt"]

for filename in filenames:
    fixed_filename = filename.replace(".","-") 
    print(fixed_filename)