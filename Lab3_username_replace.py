#program name: Lab3_username_replace.py
#author: Gnelen Mara
#purpose: a program that will replace an item in the camping listwith new item
#starter code: import the list from Lab3_gnalen_list.py
#date: 01/31/2026

from Lab3_gnalen_add import camping_items

#this code will replace items in the camping list
middle_index = len(camping_items) // 2
camping_items[middle_index] = "binoculars"

#print the updated list
print("updated length:", len(camping_items))
print("Before Binoculars added:", camping_items[:middle_index]     )
print ("Binoculars:", camping_items[middle_index])
print("After binocular:", camping_items[middle_index + 1:])
