import json
import requests

# Esegui la richiesta e converte la risposta in un oggetto JSON
response = requests.get("https://hapi.fhir.org/baseR4/Observation?subject=Patient/30163&code=3141-9")
data = response.json()

# Inizializza un array per contenere le informazioni delle osservazioni
observations_array = []

# Itera attraverso le osservazioni nel JSON
for entry in data.get('entry', []):
    observation_data = entry.get('resource', {})

    # Estrai i valori desiderati per ogni osservazione
    observation_id = observation_data.get('id', '')
    status = observation_data.get('status', '')
    code_text = observation_data.get('code', {}).get('text', '')
    effective_date_time = observation_data.get('effectiveDateTime', '')
    value = observation_data.get('valueQuantity', {}).get('value', '')
    unit = observation_data.get('valueQuantity', {}).get('unit', '')

    # Aggiungi le informazioni dell'osservazione all'array
    observation_info = [observation_id, status, code_text, effective_date_time, value, unit]
    observations_array.append(observation_info)

# Stampare l'array con le informazioni di tutte le osservazioni
print(observations_array)
