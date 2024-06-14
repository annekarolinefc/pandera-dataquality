import pandas as pd 
from faker import Faker 
import random 

fake = Faker()
num_records = 100

data = {
    "title": [fake.sentence(nb_words = 3) for _ in range(num_records)],
    "rating": [random.choice(["1E", "2E", "3E", "4E", "5E"]) for _ in range(num_records)],
    "year": [fake.year() for _ in range(num_records)],
    "runtime": [random.randint(60,180) for _ in range(num_records)]
}

df = pd.DataFrame(data)
df.to_csv("pandera/moveis.csv", index=False)
print("Arquivo 'moveis.csv' criado com sucesso")