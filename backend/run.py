# backend/run.py

# from flask import Flask
# from flask_restful import Api
# from app.resources.PollResource import PollResource  # new line

# app = Flask(__name__)
# api = Api(app)

# api.add_resource(PollResource, '/poll')  # new line

# if __name__ == '__main__':
#     app.run(debug=True)

# run.py
from dotenv import load_dotenv
load_dotenv()  # Take environment variables from .env.

from app import app

if __name__ == '__main__':
    app.run(debug=True)
