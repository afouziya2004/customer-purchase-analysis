def segment_customers(df):
    customer_revenue = df.groupby("CustomerID")["Revenue"].sum()

    segments = {
        "High Value": customer_revenue[customer_revenue > 5000],
        "Medium Value": customer_revenue[(customer_revenue <= 5000) & (customer_revenue > 2000)],
        "Low Value": customer_revenue[customer_revenue <= 2000]
    }

    return segments
