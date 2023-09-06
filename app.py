import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

headers={"authorization": os.getenv("AUTHORIZATION")}
turkoyto_payload={"type": 2, "application_id":"302050872383242240","guild_id":os.getenv("TURKOYTO_GID"), "session_id": os.getenv("SESSION_ID"),"channel_id": os.getenv("TURKOYTO_CID"), "data": {"version": "1051151064008769576", "id": "947088344167366698", "name": "bump","type": 1}}

while True:
    requests.post("https://discord.com/api/v9/interactions", headers=headers, json=turkoyto_payload)
    print("Türk Oyuncu Topluluğu öne çıkarıldı.")
    time.sleep(7200)