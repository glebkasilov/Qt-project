import os
import requests

from dotenv import load_dotenv


class ServerPartRepository:
    @classmethod
    def send_request(self, prompt: str) -> int:
        load_dotenv()
        API_KEY = os.getenv("FAL_KEY")

        input = {
            "prompt": prompt,
            "translate_input": True
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f"Bearer {API_KEY}"
        }

        url_endpoint = "https://api.gen-api.ru/api/v1/networks/kling-image"
        response = requests.post(url_endpoint, json=input, headers=headers)
        return response.json()['request_id']

    @classmethod
    def get_request(self, request_id: int) -> tuple[int, str | None]:
        load_dotenv()
        API_KEY = os.getenv("FAL_KEY")

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }

        url_endpoint = f"https://api.gen-api.ru/api/v1/request/get/{
            request_id}"
        response = requests.get(url_endpoint, headers=headers)
        response = response.json()
        print(response)
        if response['status'] == 'success':
            return (request_id, *response['result'])
        return (request_id, None)
