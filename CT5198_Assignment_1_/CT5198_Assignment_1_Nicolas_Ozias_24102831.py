# Name: Nicolas Ozias, Student ID: 24102831

# I am creating an empty list to store the number of customers each day.
customer_counts = []

for day in range(1, 8):  # It will loop for 7 days (1 to 7)
    while True:  # Keep asking until valid input is provided
        try:
            customers = int(input(f"Enter the number of customers for day {day}: "))
            if customers < 0:
                print("Please enter a positive number.")
                continue
            customer_counts.append(customers)  # Add input to the list
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Here it is calculated the maximum, minimum, and average number of customers
max_customers = max(customer_counts)
min_customers = min(customer_counts)
average_customers = sum(customer_counts) / len(customer_counts)

# Print/display results with proper rounding
print(f"Maximum customers in a day: {max_customers}")
print(f"Minimum customers in a day: {min_customers}")
print(f"Average customers per day: {round(average_customers, 2)}")
