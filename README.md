## Everything is done pretty much. Theres some left though:

1. Lock the $pay and $list to only people with `smuggler: "True"` in their jsons, along with server admins.
2. Add a command to allow the editing of user info
3. Roll into production owo
4. (optional) add a field to $check where it displays past donations (not in the current event, Ex: They paid $15 during maid revolution, and $2 during santa, rn it will display Paid: $2 Total: $17)

## Ideas for the future:

1. Simple flask website (or any other framework) to produce an easily accesible and responsive web dashboard that shows:
	- Total amount raised on top
	- List of user information (requires discord OAUTH login to see)
	- This can be expanded later on, allowing logins and having it check for smuggler role, editing data from website, etc
	- rn we just need a basic site so people can see the json thats it **Just format the json into a quick table in plain html or something and lock the page down with a password shared with everyone, then have backend update the site every once in a while.**
2. multi server support
3. allow easily setting up commands
4. this shit will never happen lmaooo




## Commands list

Yea
	- /connect
	- /pay @user amount
	- /check @user
	- /stats (list serverwide total money raised)
	- /list (list who paid more than $2)
	- /leaderboard
