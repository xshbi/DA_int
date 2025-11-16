city = input("Enter city name: ")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobbies = input("Enter your hobbies (separated by a comma): ").split(',')



print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")
print("My hobbies are:")
for hobby in hobbies:
    print(f"- {hobby.strip()}") 