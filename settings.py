import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

# OPENAI SETTINGS
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# MYSQL SETTINGS
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_PORT = os.environ.get('MYSQL_PORT')
MYSQL_DATABASE_URI = f"mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@localhost:{MYSQL_PORT}/{MYSQL_DATABASE}"