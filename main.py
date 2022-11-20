# myAgenda = []

# def printList():
#   print()
#   for item in myAgenda:
#     print(item)
#   print()

# while True:
#   menu = input("Add or Remove?: ")
#   if menu == "add":
#     item = input("Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = ("What do you want to remove?: ")
#     if item in myAgenda:
#       myAgenda.remove(item)
#     else:
#       print(f"{item} was not in the list")
#   printList()



import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n\n")
    toDoList.append(item)
  elif menu=="edit":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)