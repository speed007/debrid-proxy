from flask import jsonify
import requests
from .auth import authenticate_rd

@app.route('/torrents', methods=['GET'])
def get_torrents():
    user = authenticate_rd()  # Verify API key first
    response = requests.get(
        "https://api.real-debrid.com/rest/1.0/torrents",
        headers={"Authorization": f"Bearer {os.getenv('RD_API_KEY')}"}
    )
    return jsonify(response.json())
