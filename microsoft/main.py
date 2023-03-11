from faker import Faker
from fastapi import FastAPI, Header

app = FastAPI()

def generate_game(seed):
    fake = Faker()
    Faker.seed(seed)

    return {
        "title": fake.name(),
        "shortDescription": fake.sentence(),
        "longDescription": fake.paragraph()
    }


@app.get("/api/v1.2/jogos")
async def games(Authorization: str = Header(..., description="Authorization token")):
    return [generate_game(seed) for seed in "abcde"]