import httpx
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from datetime import datetime
from models import PokemonSet

load_dotenv()

API_URL = "https://www.pokemonpricetracker.com/api/sets"
API_KEY = os.getenv("POKEPRICE_API_KEY")

async def fetch_and_store_sets(db: Session):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()

    for item in data["data"]:
        # Parse releaseDate string to date object
        release_date = None
        if item.get("releaseDate"):
            try:
                release_date = datetime.strptime(item["releaseDate"], "%Y/%m/%d").date()
            except ValueError:
                release_date = None

        # Upsert logic (insert or update if exists)
        existing = db.query(PokemonSet).filter(PokemonSet.id == item["id"]).first()
        if existing:
            existing.name = item["name"]
            existing.series = item["series"]
            existing.printed_total = item.get("printedTotal")
            existing.total = item.get("total")
            existing.ptcgo_code = item.get("ptcgoCode")
            existing.release_date = release_date
        else:
            new_set = PokemonSet(
                id=item["id"],
                name=item["name"],
                series=item["series"],
                printed_total=item.get("printedTotal"),
                total=item.get("total"),
                ptcgo_code=item.get("ptcgoCode"),
                release_date=release_date,
            )
            db.add(new_set)

    db.commit()
