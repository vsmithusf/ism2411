# /// AI was used to assist in writing this code (Exercise 5) /// # Self-Assessment Question 3

### Notes ###
# - Exam is over conditionals, loops, and functions for second part. One page one-sided hand-written notes. 6 versions of the exam
# - Everything up to Week 8 is considered baseline for any future job, know this shit well ok? ok
# - Discount tier function most likely going to be an exam question
# - Conditionals are inside the function, functions are inside the loop -- helpful information

### Self-Assessment Questions ###
# 1) The first bug I found was the missing colon at line 10, and I noticed this before I started using tracebacks or AI to debug the code. This helped me notice that I pay good attention to the syntax of my code,
# which is a good debugging instinct that ensures that my syntax and basic structures of my code are correct.
# 2) The apply_discount function checks for which tier is inputted, and then multiplies the corresponding discount with the inputted price to return the discounted price. A colleague could likely use the function
# without reading the body because it uses simple logic that can be grasped outside of the Python language.
# 3) The AI helped me build my understanding of Python code, especially with the final error of the broken_sales file that dealt with indexing.

### Exercise 1 ###

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function
tax1 = calculate_tax(100, .07)
tax2 = calculate_tax(250, .08)

print(f"Tax on $100: ${tax1:.2f}")
print(f"Tax on $250: ${tax2:.2f}")

### Exercise 2 ###

# Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * .85
    elif tier == "silver":
        return price * .9
    elif tier == "bronze":
        return price * .95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

### Exercise 3 ###
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, .07, "gold"):.2f}")

### Exercise 4 ###
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price:.2f} | Tier: {tier} | Final: ${total:.2f}")

### Exercise 5 ###

# Fixed broken_sales.py:
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # = replaces the value of total on every pass instead of adding to it, resulting in an incorrect final amount. Using += now adds each total together and the final total is now correct.
print(f"Total: ${total}")

count = 0
for sale in sales: # : marks that the indented block belongs to the header. Without it, the code would not run because Python wouldn't know where the block begins and ends. Adding the : allows Python to
                   # separate the header and the body and the code now runs normally.
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # Because indexing starts at 0 and because the loop used <=, the loop would run from 0 to 4 and then fail while trying to run i == 5, since sales[5] is out of range. Using < instead
                      # now makes the loop stop exactly at 4, staying in range and now allowing the loop to fully complete without error.
    print(sales[i])
    i += 1

### Exercise 6 ###

x = 100 # global

def double_it():
    x = 999 # local x 
    return x * 2

print (x)
print(double_it())
print(x)