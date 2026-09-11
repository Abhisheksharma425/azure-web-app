import os
from dotenv import load_dotenv
load_dotenv()  # loads .env locally; harmless no-op once deployed to Azure

from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

@app.route("/")
def home():
    vault_url = os.environ["KEY_VAULT_URL"]
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    secret = client.get_secret("DbConnectionString")
    return f"DB secret starts with: {secret.value}..."

if __name__ == "__main__":
    app.run()