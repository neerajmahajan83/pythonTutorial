
import copy

def printloop(string):
  for s in string:
    print(s)

list = ['a','b','c','d','e']
print(printloop(list));



original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)

print(f"Original List: {original_list}")
print(f"Shallow Copied List: {shallow_copied_list}")
print(f"Deep Copied List: {deep_copied_list}")

# Modify a nested element in the shallow copy and its parent list from which shallow copy is created!
shallow_copied_list[2][0] = 99

print("\nAfter modifying shallow_copied_list[2][0]:")
print(f"Original List: {original_list}")
print(f"Shallow Copied List: {shallow_copied_list}")
print(f"Deep Copied List: {deep_copied_list}")


# Now, let's modify a nested element in the deep copy
deep_copied_list[2][1] = 88

print("\nAfter modifying deep_copied_list[2][1]:")
print(f"Original List: {original_list}")
print(f"Shallow Copied List: {shallow_copied_list}")
print(f"Deep Copied List: {deep_copied_list}")




tuple1 = ('ram','sita','hunman')
tuple2 = ('laxman',)

result = tuple1+tuple2
print(result)



name = set('ece')
print(tuple(name))



class vechile:
    def __init__(self,name,speed):
        self.__name=name
        self.__speed=speed

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def set_name(self,name):
        self.__name=name

    def set_speed(self,speed):
        self.__speed=speed


class Mahindra(vechile):
  def __init__(self,name,speed,price):
    super().__init__(name,speed)
    self.__price=price

  def get_price(self):
    return self.__price

  def set_price(self,price):
    self.__price=price

# Create a vechile object
my_vehicle = vechile("Generic Car", 120)
print(f"Vehicle Name: {my_vehicle.get_name()}")
print(f"Vehicle Speed: {my_vehicle.get_speed()} km/h")

# Create a Mahindra object
my_mahindra = Mahindra("Thar", 150, 1500000) # name, speed, price
print(f"\nMahindra Name: {my_mahindra.get_name()}") # Inherited method
print(f"Mahindra Speed: {my_mahindra.get_speed()} km/h") # Inherited method
print(f"Mahindra Price: ₹{my_mahindra.get_price()}") # Mahindra's own method

# Modify inherited attributes using inherited setter methods
my_mahindra.set_speed(160)
print(f"Mahindra New Speed: {my_mahindra.get_speed()} km/h")

# Modify Mahindra's own attribute
my_mahindra.set_price(1650000)
print(f"Mahindra New Price: ₹{my_mahindra.get_price()}")


class preppy:
  def __init__(self,name,age,std,address) :
    self.name = name
    self.age = age
    self.std = std
    self.address = address

  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  def get_std(self):
    return self.std

  def get_address(self):
    return self.address



# Create an instance of the preppy class
my_preppy_instance = preppy('Neeraj',43,15,'#628 6th floor panchkula height society. peermachula')

# Now you can access its attributes or call its methods
print(f"Preppy's name: {my_preppy_instance.get_name()}")
print(f"Preppy's address: {my_preppy_instance.get_address()}")
