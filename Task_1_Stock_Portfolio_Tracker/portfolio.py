import pandas as pd
stock_prices= {
    "AAPL": 180,   
    "TSLA": 250,   
    "GOOG": 120,   
    "AMZN": 100,   
    "MSFT": 150    
}
print(stock_prices)
number_stock=int(input("Enter Number Of Stock: "))
total=0
data=[]
for i in range(number_stock):
    stock_name = input("Enter Stock Name: ").strip().upper()
    stock_quantity = int(input("Enter Quantity: "))
    print("Stock Portfolio Report")
    if stock_name in stock_prices:
        price=stock_prices[stock_name]
        investment=price*stock_quantity
        print(f"Investment for {stock_name}: {investment}")
        total+=investment
        data.append([stock_name,stock_quantity,price,investment])
    else:
        print("Stock not found")
data.append(["total","","",total])   
df = pd.DataFrame(data, columns=["Stock", "Quantity", "Price", "Investment"])
csv_path = r"C:\quratulain.py\stock_report.csv"
# This will save the CSV in the same folder as the Python file
df.to_csv(csv_path, index=False)
print("CSV saved at:", csv_path)
print(f"Total Investment: {total}") 

