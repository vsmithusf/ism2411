### Self-Assessment Questions ###
# 1) I expected formatting lists to be a lot more complicated when I first came into class. However, I now realize that formatting and
# pulling values from a list is relatively straightforward and intuitive.
# 2) In my financial accounting class I am currently enrolled in, we've had to find the highest and lowest sale values from a large group
# of sales to perform calculations. With Python lists, finding the maximum and minimum values would be significantly easier than finding
# them by hand, which would save me time on these kinds of problems.

### Exercise 1: Build a List ###
print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

### Exercise 2: Index Practice ###
print("--- Exercise 2: Index Practice ---")

print(inventory[0]) # Always grab the first item
print(inventory[-1]) # Always grab the last item

middle = len(inventory) // 2
print(inventory[middle]) # Grabs the middle item (not hard coded)

### Exercise 3: Slicing ###
print("--- Exercise 3: Slicing ---")
### A slice always returns a new list. The original inventory remains untouched!

print(inventory[:3]) # Grabs the first three items
print(inventory[-2:]) # Grabs the last two items
print(inventory[::2]) # Skips the second and fourth items

### Exercise 4: List Methods ###
print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # Adds an item to the end of the list
inventory.append("tape")
print(inventory)

inventory.remove("tape") # Removes an item from the list (first instance if there are multiple with the same name)
print(inventory)

inventory.sort() # Sorts the list in alphabetical order permanently
print(inventory)

### Exercise 5: Tuple Comparison ###
print("--- Exercise 5: Tuple Comparison ---")

coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")

### Exercise 6: List Average Sales ###
print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f"Number of Sales: {count}")
print(f"Average Sales: {average}")
print(f"Best Sales: {max(sales)}")
print(f"Worst Sales: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

### Exercise 7: Accumulator Pattern ###
print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # Empty list
for price in prices:
    discounted.append(round(price * 0.9, 2)) # Apply a 10% discount
print(prices)
print(discounted)

### Exercise 8: Filter Above Threshold ###
print("--- Exercise 8: Filter Above Threshold ---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = [] # An empty list <--
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
