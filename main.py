import csv
import random
from faker import Faker

fake = Faker()


csv_name = 'test.csv'
num_rows = 100
fieldnames = ['First Name', 'Last Name']

with open(csv_name, 'w', newline='') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for x in range(num_rows): 
        y = str(x)
        writer.writerow({'First Name': fake.first_name(), 'Last Name': fake.last_name()})


print(f"csv_name is successfully generated!")

