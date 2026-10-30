stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks:
        investment = stocks[name] * quantity
        total += investment

        print("Stock:", name)
        print("Investment value:", investment)
    else:
        print("Stock not available!")

print("\nTotal Investment Value:", total)

file = open("portfolio.txt", "w")
file.write("Total Investment Value: " + str(total))
file.close()

print("Result saved successfully!")
