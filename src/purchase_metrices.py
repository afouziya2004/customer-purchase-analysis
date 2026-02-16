def add_revenue(df):
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    return df

def revenue_by_country(df):
    return df.groupby("Country")["Revenue"].sum().sort_values(ascending=False)

def top_customers(df, n=10):
    return df.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False).head(n)
