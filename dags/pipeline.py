from airflow.decorators import dag, task
import pendulum
from pendulum import datetime
from airflow.models import Variable
from airflow.providers.mongo.hooks.mongo import MongoHook
import json
import base64
import requests


@dag(
    start_date=datetime(2024, 11, 21),
    schedule="@daily",
    tags=["spotify_api"],
    catchup=False,
)

def pipe():
    @task
    def get_token():
        # get credentials
        client_id = Variable.get("client_id")
        client_secret = Variable.get("client_secret")

        # Codificando as credenciais em base64
        auth_string = f"{client_id}:{client_secret}"
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

        url = 'https://accounts.spotify.com/api/token'
        headers = {
            'Authorization': f'Basic {auth_base64}'
        }
        data = {
            'grant_type': 'client_credentials'
        }
        # Fazendo a solicitação POST
        response = requests.post(url, headers=headers, data=data)
        print(response.json().get('access_token'))
        return response.json().get('access_token')

    @task
    def get_playlist(token):
        url = 'https://api.spotify.com/v1/playlists/5FN6Ego7eLX6zHuCMovIR2/tracks?limit=50&offset=0'
        headers = {
        'Authorization': f'Bearer {token}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        

    @task
    def load_data_to_mongo_db(result):
        hook = MongoHook(conn_id='mongo')
        client = hook.get_conn()
        db = (
        client.spotify
        )
        currency_collection = db.currency_collection
        print(f"connected to MongoDB - {client.server_info()}")
        current_datetime = pendulum.now().to_iso8601_string()
        result["datetime"] = current_datetime
        currency_collection.insert_one(result)
    

    load_data_to_mongo_db(get_playlist(get_token()))
    #get_playlist(get_token())

pipe()