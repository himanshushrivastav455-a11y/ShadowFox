# List of friends' names
friends = ["Aditya", "Rahul", "Priya", "Anjali", "Rohan"]

# Create a list of tuples (name, length of name)
friends_with_length = []

for name in friends:
    friends_with_length.append((name, len(name)))

# Display the result
print("Friends and the length of their names:")
for friend in friends_with_length:
    print(friend)