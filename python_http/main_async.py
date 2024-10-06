import json
import aiohttp
import asyncio
from typing import List, Optional
from model import Model 

# Funktion zum Dekodieren der JSON-String zu einer Liste von Model-Instanzen
def model_from_json(json_str: str) -> List[Model]:
    data = json.loads(json_str)
    return [Model.from_json(item) for item in data]

# Funktion zum Kodieren einer Liste von Model-Instanzen zu einem JSON-String
def model_to_json(models: List[Model]) -> str:
    return json.dumps([model.to_json() for model in models])

# Asynchrone Funktion zum Abrufen der Daten
async def get_data() -> Optional[List[Model]]:
    uri = 'https://jsonplaceholder.typicode.com/posts'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(uri) as response:
                if response.status == 200:
                    json_data = await response.text()
                    print(json_data)  # Zum Debuggen
                    return model_from_json(json_data)
    except aiohttp.ClientError as e:
        print(f"Die Verbindung ist nicht verfügbar: {e}")

    return None

# Hauptfunktion zum Starten der Coroutine
async def main():
    models = await get_data()
    if models:
        for model in models:
            print(model)

# Beispielaufruf der Hauptfunktion
if __name__ == "__main__":
    asyncio.run(main())

