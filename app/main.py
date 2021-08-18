import requests
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Gelbooru(Resource):
    def get(self):
        query = request.args.get("q")
        raw_data = requests.get(f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit=1000&tags={query}")
        return raw_data.json()

api.add_resource(Gelbooru, "/gelbooru")
