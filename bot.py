#https://discordapp.com/api/oauth2/authorize?client_id=543567651130310666&permissions=8&scope=bot

import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix = "c!")
client.remove_command('help')

TOKEN = 'NTQzNTY3NjUxMTMwMzEwNjY2.Dz-e-w.lKqjY0UFpJM--4llZhZA3RKTjbY'
berryEmoji = ':strawberry:'

corgiImages = [
    'https://www.rover.com/blog/wp-content/uploads/2014/06/dogbutt.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBop55wLAmQeBNBAaSFK7-dT_t7wgYYSeNt6kqDunm8x3tq6k5mQ',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVCEib2Hh5Nf1jSV0WKnJFotlxrYw8Rl8QpTEziCJG3rNvpqgn',
    'https://assets.bhg.com/bhg/styles/nfp_1080_portrait/public/images/2017/3/15/102997431.jpg?8a7BH6ixKOPbYWfnWgBgiPbzb1SgOLfo',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975008217858059/maxresdefault.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975074441592850/6-150041-1-1471634033.png',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975086839955466/ebe0a1fd8dc05057cbea58ee546c0558.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975123758350372/ac93fb4860e77e334e289d5025f6db14.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975172819124227/images.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975213025722398/download-2.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975291823980544/download-3.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975798345039892/download-4.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975868205105162/images-2.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543975961251545100/download-5.jpg',
    'https://cdn.discordapp.com/attachments/507502888902328321/543976091405254658/images-3.jpg'
]

corgiDoryVids = [
    'https://photos.app.goo.gl/KpXA3nXQs2NBQZWi6',
    'https://photos.app.goo.gl/zz7p6pkojbApsGK16',
    'https://photos.app.goo.gl/u9Wnen24A3prTZNk9',
    'https://photos.app.goo.gl/gQiLJWGokaR6JSip8',
    'https://photos.app.goo.gl/ZAr2L4AhmQu5ZxT4A',
    'https://photos.app.goo.gl/DJDg86YXDBhxabst5',
    'https://photos.app.goo.gl/Smu96zPLmR6tjzg27',
    'https://photos.app.goo.gl/KeXzJrrSXU2j4Zsw9'
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
async def play(ctx, tp, vid):
    if tp.lower() == 'dory':
        if int(vid) > 0 and int(vid) < 8:
            await client.say("WOOF! You chose video number " + vid)
            await client.say(corgiDoryVids[int(vid)-1] + " :laughing:")
        elif int(vid) < 0:
            await client.say("WOOF! I'm only a Corgi! I can't play a number with a - in front of it!!")
        elif int(vid) > 8:
            await client.say("WOOF! I'm only a Corgi! I can't play a number that's that big!!")
        elif vid.lower() == 'trailer':
            await client.say("WOOF! You chose to watch the trailer!")
            await client.say(corgiDoryVids[7] + " :laughing:")
        elif vid == None:
            await client.say("WOOF! You need to tell me what episode you want to watch!")
        else:
            await client.say("WOOF! I can't play that!")
    elif tp == None:
        await client.say("WOOF! You need to tell me what you want to watch!")
    else:
        await client.say("WOOF! I can't play that!")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name='Corgi-Bot - Help and Documentation')
    embed.add_field(name='c!help', value='Tells you about all the commands', inline=False)
    embed.add_field(name='c!corgi_picture', value='Posts a cute photo of a corgi', inline=False)
    embed.add_field(name='c!wiki', value='View my Corgi wiki', inline=False)
    embed.add_field(name='c!play', value="Plays an episode of Corgi", inline=False)
    await client.send_message(author, embed=embed)
    await client.say("I've sent you a DM containing everything :ok_hand:")

@client.command(pass_context=True)
async def corgi_picture(ctx):
    image = random.choice(corgiImages)
    await client.say("Look at this cute corgi photo! :heart_eyes:")
    await client.say(image)

@client.command(pass_context=True)
async def wiki(ctx, char):
    if char == None:
        await client.say("WOOF!! I do have a wiki, but to use it supply an arguement after 'c!wiki'.")
    else:
        char2 = char.lower()
        if char2 == 'corgi':
            await client.say("Corgi is the one of the main characters of the corgi videos. Corgi is quite stupid, but he is very funny.")
        elif char2 == 'doby':
            await client.say("Doby is the one of the main characters of the corgi videos. Doby is obsessed with spray paint, but he loves adventuring.")
        elif char2 == 'patches':
            await client.say("Patches is the one of the main characters of the corgi videos. Patches is crazy and enjoys having fun.")
        elif char2 == 'husky':
            await client.say("Husky is the one of the main characters of the corgi videos. Husky is smart, but also quite shy.")
        elif char2 == 'scruff':
            await client.say("Scruff is the one of the main characters of the corgi videos. Scruff is somewhat smart and the most sensible of the main characters.")
        elif char2 == 'dory':
            await client.say("Dory is the antagonist in the 'Dory's in the Picture' series. Dory is mean to and hates Corgi and his friends.")
        else:
            await client.say("'" + char + "' is not in my wiki yet, or is being added. Check back soon!")

client.loop.create_task(change_status())
client.run(TOKEN)
