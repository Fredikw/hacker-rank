import pandas as pd
from datetime import datetime


'''
Question 1: Write a function to calculate the relative difference between total sales in 2017 and 2018.
'''
def relative_difference_in_sales(dataset: pd.DataFrame, year_a: int, year_b: int) -> float:

    dataset['transaction_date'] = pd.to_datetime(dataset['transaction_date'])

    # Count the number of rows for each unique value in the 'transaction_date' column
    sales_pr_year = dataset["transaction_date"].value_counts()

    print(dataset)

    # Get the count for the 'year_a' value
    sales_year_a = sales_pr_year[year_a]
    # Get the count for the 'year_b' value
    sales_year_b = sales_pr_year[year_b]

    return sales_year_b/sales_year_a - 1

'''
Question 2: Write a function to return median age per acquisition channel.
'''
def meadian_age_pr_aquisition_channel(dataset: pd.DataFrame) -> pd.DataFrame:

    # Convert the 'birth_date' strings to datetime objects
    dataset['birth_date'] = pd.to_datetime(dataset['birth_date'])

    # Calculate the age in years by subtracting the birthday from the current date
    dataset['Age'] = datetime.now().year - dataset['birth_date'].dt.year

    # Group the rows by the 'aquisition_channel' column and calculate the median 'birth_date' for each group
    median_ages = dataset.groupby('aquisition_channel')['birth_date'].median()

    return median_ages

'''
Question 3: Write a function to return the most popular product in terms of units sold among people born between start_year and end_year
'''

def get_most_popular_product_for_age_segment(customer_dataset: pd.DataFrame, order_dataset: pd.DataFrame, start_year: int, end_year: int) -> str:

    # Convert the 'birth_date' strings to datetime objects
    customer_dataset['birth_date'] = pd.to_datetime(customer_dataset['birth_date'])

    # Filter out rows where the 'birth_day' is not between the start and end years
    customer_segment = customer_dataset[customer_dataset['birth_date'].dt.year.between(start_year, end_year)]

    # Merge customer_segment and order_dataset using an inner join, orders not done by customers in customer_segment will be removed
    customer_and_order_segment = pd.merge(customer_segment, order_dataset, on='customer_id', how='inner')

    products = customer_and_order_segment.groupby('product')['quantity'].sum()

    return products.idxmax()

'''
Question 4
'''

# def name_of_function(customer_dataset: pd.DataFrame, order_dataset: pd.DataFrame):

#     order_dataset.groupby('customer_id')['revenue'].sum()


    
    
    
    
    
    # pass

# def revenue_by_year(order_dataset: pd.DataFrame) -> pd.DataFrame:

#     table = order_dataset.groupby('product').apply(lambda x: (x['quantity'] * x['price']).sum())

#     return table

# def revenue_by_customer(customer_dataset: pd.DataFrame, order_dataset: pd.DataFrame) -> pd.DataFrame:
    
#     customers_and_orders = pd.merge(customer_dataset, order_dataset, on='customer_id')

#     customers_and_orders["revenue"] = customers_and_orders["quantity"] * customers_and_orders["price"]

#     revenue_by_customer = customers_and_orders.groupby('customer_id')['revenue'].sum()

#     return(revenue_by_customer)

if __name__ == '__main__':

    # Testing relative_difference_in_sales
    order_dataset = pd.read_csv('order_test.csv')
    relativ_difference = relative_difference_in_sales(order_dataset, 2018, 2017)
    print(relativ_difference)

    # # Testing meadian_age_pr_aquisition_channel
    # customer_dataset  = pd.read_csv('customer_test.csv')
    # median_ages = meadian_age_pr_aquisition_channel(customer_dataset)
    # print(median_ages)

    # # Testing get_most_popular_product_for_age_segment
    customer_dataset  = pd.read_csv('customer_test.csv')
    order_dataset     = pd.read_csv('order_test.csv')
    # most_popular_product = get_most_popular_product_for_age_segment(customer_dataset, order_dataset, 1990, 2000)
    # print(most_popular_product)

    # name_of_function(customer_dataset, order_dataset)




    pass

# TODO Things that I must learn
# value_counts()
# groupby()
# merge()