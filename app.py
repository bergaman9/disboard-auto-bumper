import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

headers={"authorization": os.getenv("AUTHORIZATION")}
payload={"type": 2, "application_id":"302050872383242240","guild_id":os.getenv("GUILD_ID"), "session_id": os.getenv("SESSION_ID"),"channel_id": os.getenv("CHANNEL_ID"), "data": {"version": "1051151064008769576", "id": "947088344167366698", "name": "bump","type": 1}}

while True:
    requests.post("https://discord.com/api/v9/interactions", headers=headers, json=payload)
    print("Türk Oyuncu Topluluğu öne çıkarıldı.")
    time.sleep(7200)