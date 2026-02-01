#program name: Lab3_username_remove.py
#author: Gnalen Mara
#purpose: a program that will remove the last item from the camping list
#starter code: import the list from Lab3_gnalen_add.py
#date: 01/31/2026
from Lab3_gnalen_add import camping_items

#this code will remove the last item from the camping list
if "binoculars" in camping_items: 
    camping_items.remove("binoculars")

    #print out the final list of items to take on the camping trip
    print("final list", camping_items)
    print(f"Total items for the camping trip: {len(camping_items)}")