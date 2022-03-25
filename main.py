import discord #Discord libraries
import os
from keepalive import keep_alive # imports the web server that pings the bot continually
from discord.ext import commands

#client = discord.Client() # Connects to the discord client
client = commands.Bot(command_prefix = '!')
client.remove_command("help") # Removes the default "help" function to replace it by our own

@client.event #Callback to a unsychronous library of events
async def on_ready():
  # When the bot is ready to be used
  await client.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='to the sounds of the world'))

  print('Logged in as {0.user}'.format(client))

@client.event
async def on_command_error(ctx, error):
  #Handles errors
  if isinstance(error, commands.CommandNotFound): # Command not found
    await ctx.send(f'Invalid command. Try {client.command_prefix}help to search for usable commands.')
  elif isinstance(error, commands.MissingRequiredArgument): # Manque d'arguments
    await ctx.send(f'A required argument is needed. Try {client.command_prefix}help to see required arguments.')
  elif isinstance(error, commands.MissingPermissions):
    await ctx.send('You do not have the permission to do that.')
  else:
    await ctx.send("An error ocurred...")

@client.group(invoke_without_command=True, case_insensitive = True)
async def help(ctx): # Custom Help command
  embed=discord.Embed(title="Custom help command!", description="Not your boring help command ;)")
  embed.add_field(name="Hello world command", value="!helloworld")
  await ctx.send(embed=embed)

@client.command()
async def helloworld(ctx): # respond to the user
  await ctx.send(f"Hello World! {ctx.message.author.mention}")

print("Starting Bot...")

keep_alive() # Keeps the bot alive by starting a flask server

client.run(os.getenv('TOKEN')) # Runs the bot with the private bot token