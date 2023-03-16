# while loop
while True:
    fuel_status = input("Fraction ")



# print
    try :
# dayofa

        fuel_status = (fuel_status.split("/"))

# cifrebad gardaqmna

        x = int(fuel_status[0])
        y = int(fuel_status[1])

# gamotvla

        z = int((x * 100 / y))

        if z != 100 and x != 0 and z < 100:
            print(f"{z}%")
            break
        elif z == 100:
            print("F")
            break
        elif x == 0:
            print("E")
            break
        elif z > 100:
            continue
    except (ValueError, ZeroDivisionError):
        continue
    