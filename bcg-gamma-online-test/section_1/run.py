import pandas as pd
from datetime import datetime


"""""""""
Question 1: Write a function to calculate the relative difference between total sales in 2017 and 2018.
"""
def relative_difference_in_sales(dataset: pd.DataFrame, from_year: str, to_year: str) -> float:

    dataset["transaction_date"] = pd.to_datetime(dataset["transaction_date"])

    dataset["year"] = dataset["transaction_date"].dt.strftime("%Y")

    # Count the number of rows for each value in the "year" column
    sales_pr_year = dataset["year"].value_counts()

    sales_from_year = sales_pr_year[from_year]
    sales_to_year   = sales_pr_year[to_year]

    return sales_to_year/sales_from_year - 1

"""""""""
Question 2: Write a function to return median age per acquisition channel.
"""
def meadian_age_pr_aquisition_channel(dataset: pd.DataFrame) -> pd.DataFrame:

    dataset["birth_date"] = pd.to_datetime(dataset["birth_date"])

    # Calculate the age in years by subtracting the birthday from the current date
    dataset["age"] = datetime.now().year - dataset["birth_date"].dt.year

    # Group the rows by the "aquisition_channel" column and calculate the median "age" for each group
    median_ages = dataset.groupby("aquisition_channel")["age"].median()

    return median_ages

"""""""""
Question 3: Write a function to return the most popular product in terms of units sold among people born between start_year and end_year
"""

def get_most_popular_product_for_age_segment(customers: pd.DataFrame, orders: pd.DataFrame, start_year: int, end_year: int) -> str:

    customers["birth_year"] = pd.to_datetime(customers["birth_date"]).dt.year

    # Filter out rows where the "birth_year" is not between the start and end years
    customer_segment = customers[customers["birth_year"].between(start_year, end_year)]

    # Merge customer_segment and orders using an inner join
    customer__order_segment = pd.merge(customer_segment, orders, on="customer_id", how="inner")

    products = customer__order_segment.groupby("product")["quantity"].sum()

    return products.idxmax()

"""""""""
Question 4
"""
def predict_demand(customers: pd.DataFrame, orders: pd.DataFrame):

    customers_and_orders = pd.merge(customers, orders, on="customer_id", how="inner")

    customers_and_orders["revenue"] = customers_and_orders["price"] * customers_and_orders["quantity"]

    # Convert the transaction_date column to datetime and extract the year
    customers_and_orders["year"] = pd.to_datetime(customers_and_orders["transaction_date"]).dt.year

    # Group the merged DataFrame by the customer_id and year columns, and apply the sum function to the revenue column
    customer_and_year = customers_and_orders.groupby(['year', 'customer_id']).sum()['revenue']

    # Reshape the resulting DataFrame so that year is the index, customer_id is the columns, and revenue is the values
    # revenue_by_year_and_customer_id = customer_and_year.pivot_table(index='year', columns='customer_id', values='revenue')
    agg_table = customer_and_year.unstack()
    # Fill missing values with 0
    agg_table = agg_table.fillna(0)




if __name__ == "__main__":

    customers = pd.read_csv("customers.csv")
    orders    = pd.read_csv("orders.csv")

    predict_demand(customers, orders)