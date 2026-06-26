print("Hello there! Click 1 to open the Calculator:")
x = int(input())

if x != 1:
    print("Invalid choice. Program closed.")
else:
    while True:
        print("\nChoose an option:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            count = int(input("How many numbers do you want to add? "))
            total = 0

            for i in range(count):
                num = int(input(f"Enter number {i+1}: "))
                total += num

            print("Sum =", total)

        elif choice == 2:
            count = int(input("How many numbers do you want to subtract? "))

            for i in range(count):
                num = int(input(f"Enter number {i+1}: "))

                if i == 0:
                    difference = num
                else:
                    difference -= num

            print("Difference =", difference)

        elif choice == 3:
            count = int(input("How many numbers do you want to multiply? "))
            product = 1

            for i in range(count):
                num = int(input(f"Enter number {i+1}: "))
                product *= num

            print("Product =", product)

        elif choice == 4:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Division =", num1 / num2)

        elif choice == 5:
            print("Thanks for using our Calculator!")
            break

        else:
            print("Please enter a valid choice (1-5).")