def guide(): 
    global operator   
    operator=input("""
                Options:
                    For Addition, Type 1
                    For subtraction, Type 2
                    For multiply, Type 3
                    For Division, Type 4
                    For Exit, Type 0
                >>: """)
def take_input(index_of_num):
    while True:
        try:
            num = float(input(f"Enter {index_of_num} number: "))
            break
        except ValueError as e:
            print(f"Invalid Input!")
    return num

def add():
    num1 = take_input("first")
    num2 = take_input("second")
    result = num1 + num2
    print(f"The result is {result}")

def subtract():
    num1 = take_input("first")
    num2 = take_input("second")
    result = num1 - num2
    print(f"The result is {result}")

def multiply():
    num1 = take_input("first")
    num2 = take_input("second")
    result = num1 * num2
    print(f"The result is {result}")

def division():
    num1 = take_input("first")
    num2 = take_input("second")
    while num2 == 0:
        print("Enter Valid Imput!")
        num2 = take_input("second")
    result = num1 / num2
    print(f"The result is {result}")

def main():
    while True:
        guide()
        while True:
            if operator == "1":
                add()
                prompt = input("Wanna add more? (y/n): ").lower()
                if prompt != "y":
                    break
            elif operator == "2":
                subtract()
                prompt = input("Wanna subtract more? (y/n): ").lower()
                if prompt != "y":
                    break
            elif operator == "3":
                multiply()
                prompt = input("Wanna multiply more? (y/n): ").lower()
                if prompt != "y":
                    break
            elif operator == "4":
                division()
                prompt = input("Wanna divide more? (y/n): ").lower()
                if prompt != "y":
                    break
            elif operator == "0":
                print("Thank you!")
                return
            else:
                print("Enter Valid Input!")
                guide()

if __name__ == "__main__":
    main()