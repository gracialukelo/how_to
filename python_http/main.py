import requests
import json
from typing import List, Optional
from model import Model


# Funktion zum Dekodieren der JSON-String zu einer Liste von Model-Instanzen
def model_from_json(json_str: str) -> List[Model]:
    data = json.loads(json_str)
    return [Model.from_json(item) for item in data]

# Funktion zum Kodieren einer Liste von Model-Instanzen zu einem JSON-String
def model_to_json(models: List[Model]) -> str:
    return json.dumps([model.to_json() for model in models])



def get_data() -> Optional[List[Model]]:
    try:
        uri = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(uri)

        if response.status_code == 200:
            json_data = response.text
            print(json_data)  # Zum Debuggen
            return model_from_json(json_data)

    except requests.RequestException as e:
        print(f"Die Verbindung ist nicht verfügbar: {e}")

    return None



if __name__ == '__main__':
# Beispielaufruf der Funktion
    models = get_data()
    #for model in models:
        #print(model)





