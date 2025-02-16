import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv(override=True)

# Encode the password for URL
db_password = quote_plus(os.getenv('DB_PASSWORD'))

# Build the database URL
DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{db_password}" \
               f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# Create the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)