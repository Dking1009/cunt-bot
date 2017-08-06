import discord
import asyncio
import random
import json
import os
import time

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
    logEvent('INFO', "%s is logging in..." % (client.user.name))
	
def logEvent(category, message):
    if category == None:
        category = 'INFO'
    print("[%s][%s]: %s" % (time.strftime("%d/%m/%Y-%H:%M:%S"), category, message))
	
@client.event
async def on_message(message):
    # Make the message content always lowercase.
    msgContent = message.content.lower()

    # Message-triggered responses.
    if "fuck you" in msgContent and not message.author == client.user:
        await client.send_message(message.channel, "fuck YOU too %s. I hope you fucking die, cunt." % message.author)

    elif "kill myself" in msgContent or "kms" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "Yeah, you should do it. Please.")   
		
    elif "what game am i playing" in msgContent and message.author == client.user:
    	await client.send_message(message.channel, "%s you dumbfuck." % message.author.game)
		
    elif "roast me" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, random.choice(lines))
		
    elif "am i gay" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, random.choice(['yes', 'no']))

    # TODO: Make a list of commands so if we need to do ~help it will make it easier for us...

    # Developer Commands
    elif msgContent.startswith(MSG_PREFIX) and not message.author == client.user:
        if message.content == ("{0}ping".format(MSG_PREFIX)) and not message.author == client.user:
    	    await client.send_message(message.channel, "nigga, what u want?")	

        elif message.content == ("{0}src".format(MSG_PREFIX)) and not message.author == client.user:
    	    await client.send_message(message.channel, "https://github.com/NickdogeDev/cunt-bot")				
			
    # Meme Commands
    elif "<@335097025886552074>" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "What you want nigga?")
	
    elif "boneless pizza" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, ":b: O N E L E S S :b: I Z Z A")
		
    elif "lemme get uh" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, ":b: O N E L E S S :b: I Z Z A")
		
    elif "<@!106521724073304064>" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "NIGGA DONT PING THAT BITCH...")	

    elif "hello" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "Hello, %s!" % message.author)	

    elif "henlo" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "Henlo, %s!" % message.author)

    elif "helo" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "Helo, %s!" % message.author)	

    elif "hi" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "Hi, %s!" % message.author)	

    elif "sup" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "Wassup, %s?" % message.author)

    elif "whats good" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "Whats good, %s?" % message.author)

    elif "your gay" in msgContent and not message.author == client.user:
    	await client.send_message(message.channel, "I know that. Tell me something i don't know, %s" % message.author)				
	
    # New moderator mode for the bot.
    if ModeratorMode:
        logEvent('INFO', "%s said %s" % message.author, message.content)
        if msgContent in BLACKLIST_WORDS:
    	    await client.send_message(message.channel, 'Why did you say "%s"? %s.' % (message.content, message.author))
logEvent('INFO', "Running Bot...")
client.run(jdata["TOKEN"])

