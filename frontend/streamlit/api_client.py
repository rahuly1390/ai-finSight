import os
import requests


BASE_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000/api/v1"
)


def upload_document(file):

    files = {
        "file": (
            file.name,
            file,
            file.type
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

    return response.json()


def ask_agent(query):

    response = requests.post(
        f"{BASE_URL}/ask-agent",
        json={
            "query": query
        }
    )

    return response.json()