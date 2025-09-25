def gallonslit(gallon):
    return gallon * 3.78541

while True:
    gallon = int(input("Enter gallons (negative to quit): "))
    if gallon < 0:
        break
    print("Liters:", gallonslit(gallon))