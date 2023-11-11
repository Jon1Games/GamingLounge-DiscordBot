import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(
	command_prefix=commands.when_mentioned_or(),
	intents=intents,
	activity=discord.Activity(type=discord.ActivityType.playing, name='mit dem code'),
	status=discord.Status.online,
	sync_commands=True,
	delete_not_existing_commands=True
)

if __name__ == '__main__':
	print('Starting bot...')

	print('Loading cogs...')
	cogs = [file.stem for file in Path('cogs').glob('**/*.py') if not file.name.startswith('__')]
	print(f'Loading {len(cogs)} cogs...')

	for cog in cogs:
		bot.load_extension(f'cogs.{cog}')
		print(f'Loaded cog {cog}')

	token = os.getenv('TEST_BOT_TOKEN')
	bot.run(token)
