import pandas as pd

def data_transform(df_onhand: pd.DataFrame) -> pd.DataFrame:
    """Cleans and transforms the data to fit the model.

    Args:
        df_onhand (pd.DataFrame): Data to be cleaned.

    Returns:
        pd.DataFrame: Cleaned and transformed data.
    """
    
    # Transform column names to lowercase
    df_onhand.columns = df_onhand.columns.str.lower()

    return df_onhand