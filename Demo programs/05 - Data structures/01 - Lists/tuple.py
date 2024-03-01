cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total Items:', len(cars)) 
for car in cars:
    print(car)

# convert tuple to a list
car_list = list(cars)
print("Converting tuple to list:", car_list)
print("Type", type(car_list))