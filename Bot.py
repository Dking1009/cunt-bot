import discord
import asyncio
import random
import json
import os

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
    if message.content == "fuck you"  and not message.author == client.user:
    	await client.send_message(message.channel, "fuck YOU too %s. I hope you fucking die. Fucker." % message.author)
		
    elif message.content == "kill yourself" and not message.author == client.user:
    	await client.send_message(message.channel, "Yeah, you should do it. Please.")   
		
    elif message.content == "What game am i playing?" or message.content == "what game am i playing?" or message.content == "what game am i playing" or message.content == "What game am i playing" and not message.author == client.user:
    	await client.send_message(message.channel, "%s you dumbfuck." % message.author.game)
		
    elif message.content == "roast me" and not message.author == client.user:
    	await client.send_message(message.channel, random.choice(lines))  
		
    elif message.content.startswith(MSG_PREFIX) and not message.author == client.user:
        if message.content == ("{0}ping".format(MSG_PREFIX)) and not message.author == client.user:
    	    await client.send_message(message.channel, "nigga, what u want?")   
		
    	
print("Running Bot...")
client.run(jdata["TOKEN"])

