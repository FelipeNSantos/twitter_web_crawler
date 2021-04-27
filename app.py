from flask import Flask
import requests
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap

from . import apiv2
from . import process

load_dotenv('.env')

app = Flask(__name__)

bootstrap = Bootstrap(app)

apiv2.init_app(app)
process.init_app(app)

