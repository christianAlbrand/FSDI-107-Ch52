def separator():
    print("*")

# Variables
first_name = "Christian"
surname = "Albrand"
batch = 15
is_employee = True

print(first_name + " " + surname + " #" + str(batch))

count = 30
price = 7.99
message = "Good Morning"
is_open = False

separator()

# Type conversion
balance = 19.99
print(int(balance))

year = 2023
print(str(year))

temperature = "98.6"
print(float(temperature))

# Challenge
name = "Martha"
last_name = "Lee"
age = 45
print("Hello " + name + " " + last_name + ", you are " + str(age) + " years old.")

separator()

# Operators
a = 7
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

separator()

# Comparison Operators
p = 15
q = 10

print(p == q)
print(p != q)
print(p > q)
print(p < q)
print(p >= q)
print(p <= q)

x = 8
y = 20
print(x > 5 and y < 25)
print(x < 5 or y > 15)
print(not(x == 8))

separator()

# Lists
vehicles = ["car", "bike", "bus"]
print(vehicles)
print(vehicles[0])
print(vehicles[-1])

vehicles.append("train")
print(vehicles)

vehicles.remove("bike")
print(vehicles)

print(vehicles.pop(1))
print(vehicles)

print(vehicles.index("car"))

vehicles.append("car")
print(vehicles)
print(vehicles.count("car"))

separator()

# If statements
age = 17
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

speed = 55

if speed > 60:
    print("Over speed limit")
elif speed == 60:
    print("At speed limit")
else:
    print("Below speed limit")

for i in range(4):
    print(i)

cities = ["New York", "Paris", "Tokyo"]

for city in cities:
    print(f"City: {city}")

separator()

# Functions
def say_hello():
    print("Hello from say_hello function")

say_hello()

def welcome_person(name):
    print("Welcome, " + name)

welcome_person("Jordan")