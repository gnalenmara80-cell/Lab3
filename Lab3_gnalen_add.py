#program Name: Lab3_gnalen_add.py
#Author : Gnalen Mara
#purpose: a program that will add 5 items to an existing list of camping items
#starter code: import the list from Lab3_gnalen_list.py
#Date: 01/31/2026

from Lab3_gnalen_list import camping_items

#added 5 more items to the camping list
camping_items.append("Stove")
camping_items.append("Rope")
camping_items.append("Gloves")
camping_items.append("Sunscreen")
camping_items.append("Knife")

#print the updated list
print(sorted(camping_items, reverse=True))

