import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # 1. Case of empty
    if orders.shape[0] == 0:
        return orders[['customer_number']]
    
    # 2. Count order
    orders = orders.groupby('customer_number').count()
    
    # 3. Sort from large to small
    orders.sort_values(by='order_number',ascending=False, inplace=True)

    return orders.reset_index().iloc[[0]][['customer_number']]
