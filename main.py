# main.py
import logging
from scripts.data_process import process_file

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        # Caminho do arquivo .xlsx de origem
        xlsx_file = r"C:\Users\Paulo\Downloads\Downloads-1\Integration Onhand Inquiry20250113.xlsx"
        # Processar o arquivo
        process_file(xlsx_file)
    except Exception as e:
        logging.error(f"An error occurred during the execution of the process: {e}")
        logging.exception("Error details: ")

if __name__ == "__main__":
    main()