# process_data.py
import os
import logging
import pandas as pd
import win32com.client
from scripts.db_connection import SessionLocal, engine
from scripts.models import Base
from scripts.data_transformation import data_transform
from scripts.db_operations import save_to_db

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_file_date(xlsx_file):
    excel = win32com.client.Dispatch("Excel.Application")
    wb = excel.Workbooks.Open(xlsx_file, ReadOnly=True)
    last_save_time = wb.BuiltinDocumentProperties("Last Save Time").Value
    wb.Close()
    excel.Quit()
    return last_save_time.strftime('%Y-%m-%d %H:%M:%S')
    
def process_file(xlsx_file):
    # Create tables in the database
    Base.metadata.create_all(bind=engine)

    # Create session
    db = SessionLocal()

    try:
        
        # Load the data
        with pd.ExcelFile(xlsx_file) as xls:
            df_onhand = xls.parse()

        # Extract file date
        plan_date = get_file_date(xlsx_file)
    
        # Clean the data
        df_onhand = data_transform(df_onhand)

        # Save to the database
        save_to_db(df_onhand, db, plan_date)
    except Exception as e:
        logging.error(f"An error occurred during the execution of the process: {e}")
        logging.exception("Error details: ")
    finally:
        # Delete the converted file to avoid accumulation
        if xlsx_file and os.path.exists(xlsx_file):
            try:
                #os.remove(xlsx_file)
                logging.info(f"Temporary file removed: {xlsx_file}")
            except Exception as e:
                logging.error(f"Could not delete the file: {e}")

        # Close the database connection
        db.close()