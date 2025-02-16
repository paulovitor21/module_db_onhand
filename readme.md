# OnHand Inventory Management

## Overview
OnHand: typically refers to the currently available inventory.

### Significance of the "OnHand" Spreadsheet
- **Represents the quantity of materials, components, or finished products that are physically available in the factory's stock or warehouses.**
- **Used for inventory control, helping the Sourcing team assess whether there are enough materials to meet production needs or if new purchases are required.**


### Relationship with Material Requirements Planning (MRP)
- The OnHand spreadsheet is crucial for MRP (Material Requirements Planning) as it allows comparison of available stock with future demand.
- If the OnHand quantity is below the required level, the system can generate purchase or production orders.
- It also helps manage excess and obsolescence, avoiding unnecessary stock.

## Project Structure
This project automates the process of loading, transforming, and saving the OnHand inventory data into a database.

### Main Components
- **main.py**: Entry point of the application.
- **data_process.py**: Handles the loading, transformation, and saving of data.
- **db_connection.py**: Manages the database connection.
- **db_operations.py**: Contains functions to save data to the database.
- **data_transformation.py**: Cleans and transforms the data to fit the model.

## Usage
1. **Configure the database connection**: Ensure the `.env` file contains the correct database credentials.
2. **Run the main script**: Execute `main.py` to process the OnHand spreadsheet and save the data to the database.

### Example
```bash
python main.py