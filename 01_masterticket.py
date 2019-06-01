TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  

def calculate(number):
	return (number * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >0:
	print("There are {} tickets remainig".format(tickets_remaining))
	user_name = input("What's your name?  ")
	number_of_tickets = input ("{} how many ticket would you like to buy?  ".format(user_name))
	# Expect ValueError if it would be not number
	try:
		number_of_tickets = int(number_of_tickets)
		# Raise a ValueError if the request is for more tickets than are avalible
		if tickets_remaining<number_of_tickets:
			raise ValueError("There are only {} tickets remainning".format(tickets_remaining))
	except ValueError as err:
		# Include the error text in input
		print("Oh no there is {}. Enter a valid number of tickets".format(err))
	else:	
#		price = number_of_tickets * TICKET_PRICE
		price = calculate(number_of_tickets)
		print ("That would be {} $".format(price))
		decision = input("You want to proceed? (Y/N)   ")
		decision = decision.lower()
		if decision == "y":
			print ("SOLD!")
			tickets_remaining -= number_of_tickets
		else:
			print("Thanks {}".format(user_name))
print ("Sorry, tickets are sold out!")
