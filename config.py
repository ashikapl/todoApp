from dotenv import load_dotenv
import pymysql
import os

# Load environment variables
load_dotenv()

# Connect to todo database
DB_CONFIG = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)