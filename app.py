from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)


print("=== Initializing Services ===")
db_url = os.getenv('DB_URL')
print("=== Initializing API ===")
