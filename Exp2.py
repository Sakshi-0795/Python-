consumer_id = input("Enter Consumer ID: ")
consumer_name = input("Enter Consumer Name: ")
units = float(input("Enter Units Consumed: "))

energy_charge = 0.0
fixed_charge = 50.0  

if units <= 100:
    energy_charge = units * 1.50
elif units <= 200:
    energy_charge = (100 * 1.50) + ((units - 100) * 2.50)
elif units <= 300:
    energy_charge = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
else:
    energy_charge = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((units - 300) * 6.00)

tax = energy_charge * 0.05
total_bill = energy_charge + fixed_charge + tax

print("\n" + "=" * 40)
print("           ELECTRICITY BILL")
print("=" * 40)
print(f"Consumer ID     : {consumer_id}")
print(f"Consumer Name   : {consumer_name}")
print(f"Units Consumed  : {units:.2f} kWh")
print("-" * 40)
print(f"Energy Charges  : ₹{energy_charge:.2f}")
print(f"Fixed Charges   : ₹{fixed_charge:.2f}")
print(f"Tax (5%)        : ₹{tax:.2f}")
print("-" * 40)
print(f"Total Amount    : ₹{total_bill:.2f}")
print("=" * 40)
