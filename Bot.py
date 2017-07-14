import discord
import asyncio
import random
import json
import os

CMD_LIST = ['ping', 'help']

# Description of each command
CMD_DESC = {
'help': 'If you need help with the command.',
'ping': 'Ping the bot to determine if its alive or not.'
}

# Enable this to 'True' if you want the bot to moderate logs.
# TODO: Remove messages if its in the chat blacklist..
ModeratorMode = True

# No words right now..
# TODO: Load the blacklist from a txt file or something alike..
BLACKLIST_WORDS = []

JSON_FILENAME = 'data/config.json'
ROAST_FILENAME = 'data/roasts.txt'
MSG_PREFIX = "~"
client = discord.Client()
# Randomize the list of insults from the file
client.change_status(discord.Game(game='Say "roast me" to be roasted..'))
lines = open(ROAST_FILENAME).read().splitlines()

# Load the JSON config
if not os.path.exists(JSON_FILENAME):
    with open(JSON_FILENAME, 'w+') as file:
        fields = {"TOKEN": 'insert token here'}
        json.dump(fields, file)

jsonFile = open(JSON_FILENAME, 'r+')
jdata = json.load(jsonFile)
	 
@client.event
async def on_ready():
    print("%s is logging in..." % (client.user.name))
	
@client.event
async def on_message(message):
    # This is a bit messy, should be cleaned up and reorganized soon.
    msgContent = message.content.lower()
    if "fuck you" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "fuck YOU too %s. I hope you fucking die. Fucker." % message.author)
		
    elif "kill myself" in msgContent or "kms" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "Yeah, you should do it. Please.")   
		
    elif "what game am i playing" in msgContent and message.author == client.user:
    	await client.send_message(message.channel, "%s you dumbfuck." % message.author.game)
		
    elif "roast me" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, random.choice(lines))
		
    elif "am i gay" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, random.choice(['yes', 'no']))
		
	# TODO: Make a list of commands so if we need to do ~help it will make it easier for us...
    elif msgContent.startswith(MSG_PREFIX) and not message.author == client.user:
        if message.content == ("{0}ping".format(MSG_PREFIX)) and not message.author == client.user:
    	    await client.send_message(message.channel, "nigga, what u want?")			
			
    elif "<@335097025886552074>" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "What you want nigga?")
	
    elif "boneless pizza" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, ":b: O N E L E S S :b: I Z Z A")
		
    elif "lemme get uh" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, ":b: O N E L E S S :b: I Z Z A")
		
    elif "<@!106521724073304064>" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "NIGGA DONT PING THAT BITCH...")		
	
    # New moderator mode for the bot.
    if ModeratorMode and not message.author == client.user:
        print("[INFO]: %s said %s" % (message.author, msgContent))
        if msgContent in BLACKLIST_WORDS:
    	    await client.send_message(message.channel, 'Why did you say "%s"? %s.' % (message.content, message.author))   
			
    if message.author == client.user:
        print("[BOT DEBUGGING]: %s said %s" % (message.author, msgContent))            			
    	
print("Running Bot...")
client.run(jdata["TOKEN"])

