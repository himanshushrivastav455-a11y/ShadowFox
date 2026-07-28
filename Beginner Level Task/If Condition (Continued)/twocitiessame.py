# Lists of cities
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# User input
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check if both cities are in the same country
if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
elif city1 in India and city2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")