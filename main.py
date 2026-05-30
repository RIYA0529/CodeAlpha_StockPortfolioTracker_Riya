print("STOCK PORTFOLIO TRACKER")

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 300
}

stock = input("Enter Stock Name: ").upper()
quantity = int(input("Enter Quantity: "))

if stock in stocks:
    total = stocks[stock] * quantity
    print("Total Investment Value =", total)
else:
    print("Stock Not Found")