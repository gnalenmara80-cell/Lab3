#program name: Lab3_gnalen_list.py
#Author: Gnalen Mara
#purpose: create a program with a list of strings containing exactly 10 camping items, that will output the list in alphabetical order, and output the number of items in the list.
#starter code: none
#Date: 01/31/2026
camping_items = [
    "Tent",
    "Sleeping Bag",
    "First Aid Kit",
    "Falshlight",
    "blanket",
    "Water",
    "Food",
    "Map",
    "Compass",
    "Insect Repellent"
]
#print the total number of item in the list
print(f"number of items in the list: {len(camping_items)}")
#this will output the list in alphabetical order
print("items in alphabetical order:", sorted(camping_items))