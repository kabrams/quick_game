import random


s1="Rock"
s2="Paper"
s3="Scissors"

def rules(users_choice, computers_choice):

	if users_choice == s1 and computers_choice == s1:
		return f"You picked {users_choice} and the computer picked {computers_choice}, it's tied."
	if users_choice == s1 and computers_choice == s2:
		return f"You picked {users_choice} and the computer picked {computers_choice}, you lose!"
	if users_choice == s1 and computers_choice == s3:
		return f"You picked {users_choice} and the computer picked {computers_choice}, you win!!"
	if users_choice == s2 and computers_choice == s2:
		return f"You picked {users_choice} and the computer picked {computers_choice}, it's tied."
	if users_choice == s2 and computers_choice == s3:
		return f"You picked {users_choice} and the computer picked {computers_choice}, you lose!"
	if users_choice == s2 and computers_choice == s1:
		return f"You picked {users_choice} and the computer picked {computers_choice}, you win!!"
	if users_choice == s3 and computers_choice == s3:
		return f"You picked {users_choice} and the computer picked {computers_choice}, it's tied."
	if users_choice == s3 and computers_choice == s1:
		return f"You picked {users_choice} and the computer picked {computers_choice}, you lose!"
	if users_choice == s3 and computers_choice == s2:
		return f"You picked {users_choice} and the computer picked {computers_choice}, you win!!"

options = ['Rock', 'Paper', 'Scissors']


