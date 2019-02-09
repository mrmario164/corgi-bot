import discord
from discord.ext import commands
import asyncio
from itertools import cycle

client = commands.Bot(command_prefix = "c!")

TOKEN = 'NTQzNTY3NjUxMTMwMzEwNjY2.Dz-e-w.lKqjY0UFpJM--4llZhZA3RKTjbY'

statusmsg = ["c!help - Get to know server commands with this one! WOOF!!"]

async def change_status():
    await client.wait_until_ready()
    messages = cycle(statusmsg)

    while not client.is_closed:
        current_status = next(messages)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(4)

@client.event
async def on_ready():
    print("I'm a cooooooooooorgi!! Ready to go!")

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

client.loop.create_task(change_status())
client.run(TOKEN)
