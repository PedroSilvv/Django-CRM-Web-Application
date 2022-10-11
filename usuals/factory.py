import random
from unicodedata import digit
from faker import Faker

fake = Faker()

def rand_ratio():
    return random.randint()

def create_random_CRM():
    return {
        'id' : fake.random_number(digits=4),
        'data' : fake.date(),
        'colaboradores' : fake.random_number(),
    }

#print(fake.random_number(digits=4))
#print(fake.date())