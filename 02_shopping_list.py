shopping_list =[]


def add_to_list(item):
	shopping_list.append(item)
	print("There are {} items on list".format(len(shopping_list)))

	
def show_help():
	print("what should we pick up at the store?")
	print("""
Enter "DONE" to stop adding items.
Enter "HELP" for this help.
Enter "SHOW" for shopping list.
""")
	
def show_list():
	print(*shopping_list, sep = "\n")

show_help()

while True:
	new_item = input("> ")
	if new_item == "DONE":
		break
	elif new_item == "HELP":
		show_help()
		continue
	elif new_item == "SHOW":
		show_list()	
		continue
	add_to_list(new_item)
show_list()
