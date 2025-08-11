import pandas as pd

def fill_missing_arrival_with_departure(df):
    """Fill missing 'Arrival Delay in Minutes' with 'Departure Delay in Minutes'."""
    mask = df['Arrival Delay in Minutes'].isna()
    df.loc[mask, 'Arrival Delay in Minutes'] = df.loc[mask, 'Departure Delay in Minutes']
    return df


def drop_columns(df, cols_to_drop):
    """Drop specified columns from dataframe."""
    df.drop(columns=cols_to_drop, inplace=True, errors='ignore')
    return df


def reorder_columns(df, priority_cols):
    """Reorder columns for better readability."""
    sort_col = df[priority_cols]
    other_col = [col for col in df.columns if col not in priority_cols]
    df = pd.concat([sort_col, df[other_col]], axis=1)
    return df


def clean_column_names(df):
    """Convert column names to lowercase and replace hyphens with spaces."""
    df.columns = df.columns.str.lower().str.replace('-', ' ')
    return df


def convert_column_type(df, column, new_type):
    """Convert a column to a new data type."""
    df[column] = df[column].astype(new_type)
    return df
