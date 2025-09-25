airports = {}
while True:
    print("\n1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
    elif choice == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")