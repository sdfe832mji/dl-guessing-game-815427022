# Your existing lists (or items inside seller lists)
orange = ["navel", "blood orange"]
lemon = ["meyer", "eureka"]
tomato = ["roma", "cherry", "beefsteak"]

# Map each seller to what they sell
sellers = {
    "james": ["tomato", "orange"],
    "sarah": ["lemon", "orange"],
    "mike": ["tomato"]
}

search_item = input("What are you looking for? ").lower()

# Find all sellers who have that item in their list
matching_sellers = [seller for seller, items in sellers.items() if search_item in items]

# Print the result
if matching_sellers:
    for seller in matching_sellers:
        print(f"{seller.capitalize()} sells {search_item}.")
else:
    print(f"Nobody sells {search_item}.")
