import pandas as pd

def generate_dim_date_csv(start_year=2010, end_year=2040, file_name="dim_date.csv"):
    """
    Generate a CSV file containing date dimension data from start_year to end_year.
    """
    # Generate all dates from start_year to end_year
    date_range = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq='D')

    # Create DataFrame
    df = pd.DataFrame({"date": date_range})

    # Add computed columns
    df["monthId"] = df["date"].dt.month
    df["dayOfWeek"] = df["date"].dt.weekday + 1  # Adjusting Monday=0 to Monday=1
    df["dayOfMonth"] = df["date"].dt.day
    df["dayOfYear"] = df["date"].dt.dayofyear
    df["isWorkingDay"] = df["dayOfWeek"] <= 5  # Monday to Friday are working days

    # Save to CSV
    df.to_csv(file_name, index=False)

    print(f"CSV file '{file_name}' created successfully with {len(df)} rows.")

# Run the function
generate_dim_date_csv()
