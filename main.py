a = "apple"
one = None
while True:
	one = input("Please enter your password: ")
	if one == a:
		print("Correct!")
		break
	else:
		print("Incorrect, try again\n")
	# The while loop will loop-over again
#

print("\n You win... a Cookie!")