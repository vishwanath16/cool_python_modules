from faker import Faker
import csv

fake = Faker()

n_records = 100
csv_file = "fake_data.csv"
field_names = ['Name', 'Address', 'Phone Number', 'Email']


with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()

    for _ in range(n_records):
        fake_name = fake.name()
        fake_address = fake.address()
        fake_phone_number = fake.phone_number()
        fake_email = fake.email()
        writer.writerow({'Name': fake_name, 'Address': fake_address, 'Phone Number': fake_phone_number, 'Email': fake_email})

print(f"CSV File '{csv_file}' generated successfully with {n_records} records.")