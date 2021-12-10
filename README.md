# TO-DO

Need: User registration system (/connect) where they can input their real name and grade. **DONE, BUT NEEDS POLISHING** (bot accepts message from anyone as input, will be a problem. someone pls lock it down to ctx.author for me)

Smugglers need their own registration, done manually, to log the amount of money they earned.

1.  Allow users to request a payment deposit (/pay)

	- Respond with the list of Money Smugglers, and then link them to the channel with their schedules
	- After they pick a smuggler, have the bot dm the smuggler that the user picked with the User name and grade information.
	- After that is done, the bot will create a new channel in the server and allow the user to speak with the smuggler and complete the deal. Add /close for convenience of ticketing.
	- After the transaction is done, smuggler can run /finish {user} {amount} and log to a json file. The sums will also be logged to the smuggler's account, to make money tracking simplified.
	- Json file should add to the user dictionary the amount that they paid, who they paid to, and when.
	

2. Allow checking of money balances and stats per user **PARTIALLY DONE, $check already exists, but someone should let it accept an arg if an admin runs it ($check @ling)**

	- /check {@user} should allow people to check that user's stats, such as name, grade, money paid, etc. Smugglers need their own output. (Add something in the json to separate smugglers from users, and use if statement to verify)
	- Users can only check their own stats, unless they are admin.
	- /stats should show serverwide statistics, such as total money raised. Anyone can use it. **Stats aren't done yet**

3. List users who paid

	- listpaid should be owner only. DMs a full list of students who paid their dues to simplify distribution. Also display the total amount of people at the bottom, for simplified buying.

## Commands list

	- /connect
	- /pay
	- /finish
	- /check
	- /stats
	- /listpaid
