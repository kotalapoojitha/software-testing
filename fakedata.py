from faker import Faker
from faker.proxy import Faker
fake = Faker()

for i in range(5):
    print(f"Name    : {fake.name()}")
    print(f"Email   : {fake.email()}")
    print(f"Phone   : {fake.phone_number()}")
    print(f"Address : {fake.address()}")
    print("-" * 40)