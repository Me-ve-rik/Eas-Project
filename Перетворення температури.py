temp = float(input("Введіть температуру: "))
scale = input("Введіть шкалу (C/F): ").upper()

if scale == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit:.2f}°F")
elif scale == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F = {celsius:.2f}°C")
else:
    print("Невірна шкала.")
