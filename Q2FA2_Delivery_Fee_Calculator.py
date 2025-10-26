distance = float(input('Enter distance in kilometers: '))
rate_of_charge = float(input('Enter rate per kilometer (₱): '))
print(f'Total Deliver Fee: ₱{round((distance * rate_of_charge),2)}.')