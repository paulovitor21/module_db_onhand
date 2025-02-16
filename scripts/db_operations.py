from sqlalchemy.orm import Session
from scripts.models import OnhandRecord
import logging

def save_to_db(df_onhand, db: Session, file_date):
    """
    Saves records to the database using ORM.
    Processes all records, but only non-duplicate records will be inserted into the database.

    Args:
        df_onhand (DataFrame): DataFrame with the data to be inserted.
        db (Session): Database session.
    """

    # Convert all columns to string
    df_onhand = df_onhand.astype(str)
    # Check if records already exist in the database for the same file date
    existing_records = db.query(OnhandRecord).filter_by(file_date=file_date).first()
    
    if existing_records:
        logging.info(f"[Ignored] Records for the date {file_date} already exist in the database. No records were inserted.")
        return False  # No data was inserted
    
    # Insert the records, as there are no records for the file date
    inserted_count = 0

    for _, row in df_onhand.iterrows():
        
        record = OnhandRecord(
            file_date = file_date,
            org = row['org'],
            item = row['item'],
            uit = row['uit'],
            uom = row['uom'],
            desc = row['desc'],
            spec = row['spec'],
            subinv = row['subinv'],
            locator = row['locator'],
            onhand_qty = row['onhand qty'],
            reserve_qty = row['reserve qty'],
            available = row['available'],
            item_cost = row['item cost'],
            amount = row['amount'],
            small_packing = row['small packing'],
            w_keeper = row['w-keeper'],
            planner = row['planner'],
            purchaser = row['purchaser'],
            location = row['location'],
            delivery_type = row['delivery type'],
            sub_mat = row['sub mat'],
            wms_flag = row['wms flag']
        )
        db.add(record)
        inserted_count += 1  # Increment the count of inserted records

    # Commit to the database
    db.commit()
    # Display success message only if records were inserted
    logging.info(f"[Inserted] Total records inserted for the date {file_date}: {inserted_count}.")
    logging.info("Data saved successfully!")
    return True