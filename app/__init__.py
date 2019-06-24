from flask import Flask
import os.path as op
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

from app import routes