def check_adult(age):
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are not an adult.")

if __name__ == "__main__":
    age = int(input("Enter your age: "))
    check_adult(age)
