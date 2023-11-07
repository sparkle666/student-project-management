import random
import faker
from pages.models import Hotel

fake = faker.Faker()

def generate_fake_hotel_data(number_of_records):
    for _ in range(number_of_records):
        hotel = Hotel()
        hotel.name = fake.company()
        hotel.description = fake.paragraph()
        hotel.rating = random.choice([i for i in range(6)])
        hotel.price = round(random.uniform(50, 5000), 2)
        hotel.save()
        print(f"Generated {hotel.name} success!")

# Example usage: Generate 10 fake hotel records
generate_fake_hotel_data(1)
