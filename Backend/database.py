import os

import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
  return pymysql.connect(
    host=os.environ["DB_HOST"],
    port=int(os.getenv("DB_PORT", "3306")),
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"],
    cursorclass=pymysql.cursors.DictCursor,
    connect_timeout=5
  )
