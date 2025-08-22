
# 1. Hardcoded stock prices (Dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}  # Dictionary to store user portfolio

print("📈 Welcome to Stock Portfolio Tracker 📈")
print("Available Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# 2. Taking user input (Stock name + Quantity)
while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("⚠ Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # Add stock to portfolio
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

# 3. Basic arithmetic: Calculate total investment
total_value = 0
print("\n🧾 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock} ({qty} shares) -> ${value}")

# 4. Output: Display total investment
print(f"\n💰 Total Investment Value: ${total_value}")

# 5. File Handling (optional: save results)
choice = input("\nDo you want to save the result? (y/n): ").lower()
if choice == "y":
    filename = input("Enter filename (portfolio.txt or portfolio.csv): ")
    if filename.endswith(".csv"):
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
            f.write(f"Total,,,${total_value}\n")
    else:  # default txt file
        with open(filename, "w") as f:
            f.write("Your Stock Portfolio:\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock} ({qty} shares) -> ${stock_prices[stock]*qty}\n")
            f.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"✅ Portfolio saved to {filename}")
