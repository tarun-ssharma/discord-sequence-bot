import os
import discord
import configparser
from discord.ext import commands
import requests

config = configparser.ConfigParser()
config.read('discord.ini')
TOKEN = config.get('DISCORD','TOKEN')
GUILD = config.get('DISCORD','GUILD_NAME')

bot = commands.Bot(command_prefix='/')

@bot.command(name='s', help="detects sentiment of the given text")
async def hundred(ctx, nums: str):
	next_three = ''
	try:
		sequences = requests.get('http://oeis.org/search?fmt=text&q={}'.format(nums)).text.splitlines()
		print(sequences)
		for seq in sequences:
			if nums in seq:
				index_next = seq.index(nums) + len(nums) + 1
				curr = index_next
				length = len(seq)
				num_comma = 0
				while(curr<length):
					if(seq[curr] == ','):
						num_comma +=1
						if(num_comma == 3):
							break
					next_three += seq[curr]
					curr += 1
				if(len(next_three)!=0):
					break
		if next_three == '':
			next_three = 'No sequence found!'
		await ctx.send(next_three)
	except Exception as e:
		raise discord.DiscordException



bot.run(TOKEN)
