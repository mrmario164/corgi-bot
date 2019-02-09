#https://discordapp.com/api/oauth2/authorize?client_id=543567651130310666&permissions=8&scope=bot

import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix = "c!")
client.remove_command('help')

TOKEN = 'NTQzNTY3NjUxMTMwMzEwNjY2.Dz-e-w.lKqjY0UFpJM--4llZhZA3RKTjbY'

corgiImages = [
    'https://www.rover.com/blog/wp-content/uploads/2014/06/dogbutt.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBop55wLAmQeBNBAaSFK7-dT_t7wgYYSeNt6kqDunm8x3tq6k5mQ',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVCEib2Hh5Nf1jSV0WKnJFotlxrYw8Rl8QpTEziCJG3rNvpqgn',
    'https://assets.bhg.com/bhg/styles/nfp_1080_portrait/public/images/2017/3/15/102997431.jpg?8a7BH6ixKOPbYWfnWgBgiPbzb1SgOLfo'
]

async def change_status():
    await client.wait_until_ready()

    while not client.is_closed:
        await client.change_presence(game=discord.Game(name="c!help - Get to know server commands with this one!"))
        await asyncio.sleep(4)

@client.event
async def on_ready():
    print("I'm a corgi!! Ready to go!")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name='Corgi-Bot - Help and Documentation')
    embed.add_field(name='!help', value='Tells you about all the commands', inline=False)
    embed.add_field(name='!photo', value='Posts a cute photo of a corgi', inline=False)
    await client.send_message(author, embed=embed)
    await client.say("I've sent you a DM containing everything :ok_hand:")

@client.command(pass_context=True)
async def corgi_image(ctx):
    image = random.shuffle(corgiImages)[0]
    await client.say("Look at this cute corgi photo! :heart_eyes:")
    await client.say(image)

client.loop.create_task(change_status())
client.run(TOKEN)
