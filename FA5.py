print('Enter your destinations for today: ')
destinations = [ ]

for i in range(5):
     place = input(f'Enter destination {i+1}: ')
     destinations.append(place)
#"\n" adds a blank line which makes the output clean and organized"
print('\nOriginal travel itinerary; ')

for i, place in enumerate(destinations, start=1):
    print(f'{i}. {place}')

print("\nLet's update your 2nd and 5th travel destinations.")
new_2 = input('Enter new 2nd destination: ')
destinations[1] = new_2
new_5 = input("Enter new 5th destination: ")
destinations[4] = new_5
print('\nUpdated travel itinerary: ')
for i, place in enumerate(destinations, start=1):
    print(f"{i}. {place}")
