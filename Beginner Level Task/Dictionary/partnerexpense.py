# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

# Print total expenses
print("Your Total Expenses:", your_total)
print("Partner's Total Expenses:", partner_total)

# Determine who spent more
if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent more money overall.")
else:
    print("Both of you spent the same amount.")

# Find the category with the maximum spending difference
max_difference = 0
max_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        max_category = category

# Print the category with the greatest difference
print("Category with the highest spending difference:", max_category)
print("Difference:", max_difference)