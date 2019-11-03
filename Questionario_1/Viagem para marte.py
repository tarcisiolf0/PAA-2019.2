def search(takeoff, landing, height, size, fuel):
    best_fuel = fuel
    for i in range(size):
        coe_landing = (height + fuel) / landing[i]
        coe_takeoff = (height + fuel) / takeoff[i]
        fuel = fuel - coe_takeoff - coe_landing
        print("Coe_landing {0:.2f} | Coe_takeoff {1:.2f} | Fuel {2:.2f}".format(
                coe_landing, coe_takeoff, fuel))

    print("Best_Fuel {0:.2f}".format(best_fuel))
    if fuel == 0:
        return best_fuel
    if fuel > 0:
        search(takeoff, landing, height, size, best_fuel / 2)
    elif fuel < 0:
        return best_fuel

    return best_fuel

size = int(input())
height = int(input())
aux = input().split(" ")
takeoff = [int(num) for num in aux]
aux = input().split(" ")
landing = [int(num) for num in aux]
fuel = 1000000000
result = search(takeoff, landing, height, size, fuel)
if fuel > 1000000000:
    print('-1')
else:
    print(result)