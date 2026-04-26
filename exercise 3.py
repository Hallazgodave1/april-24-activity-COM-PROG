try:
    # user input (keep in mind boi)
    username = input("Enter Username: ")
    age = int(input("Enter Age: "))
    
    #  input
    if username == "":
        print("Error: Username cannot be empty.")
    elif age <= 0:
        print("Error: Age must be greater than 0.")
    else:
        
        
        # file save 
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")

        print("\nUser saved successfully!")

        # Display all saved users
        print("\nSaved Users:")
        with open("users.txt", "r") as file:
            for line in file:
                print(line.strip())

except ValueError:
    print("Error: Age must be a number.")

except FileNotFoundError:
    print("Error: File not found.")

finally:
    print("\nSystem complete.")
    