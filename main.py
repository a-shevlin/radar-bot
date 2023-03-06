import os
import time

import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('TOKEN')
CHANNEL_ID=os.getenv('CHANNEL_ID')
USER_ID=os.getenv('USER_ID')
BOT_ID=int(os.getenv('BOT_ID'))

MUTE_DURATION = 10

intents = discord.Intents.default()

client = discord.Client(intents=intents)

bot = commands.Bot(intents=intents, command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_voice_state_update(member, before, after):
    # print(member.id)
    if after.channel.id != None and before.channel.id != int(CHANNEL_ID) and after.channel.id == int(CHANNEL_ID) and member.id == int(USER_ID):
        message = f"{member.name} has joined {after.channel.name}!"
        await member.edit(mute=True)
        #   WIP send message
          #  TODO implement message only on join and not other states
        for member in after.channel.members:
            if member.id != int(USER_ID):
              print(message, 'to ', member)
              await member.send(message)  
        await asyncio.sleep(MUTE_DURATION)
        await member.edit(mute=False)

        # WIP Loop to Check for bot in channel
            # TODO make bot leave or timeout after 10 seconds
        # members = []
        # for member in after.channel.members:
        #     members.append(member.id)
        # if BOT_ID not in members:
        #   await after.channel.connect()
          # await vc.voice_disconnect()
          # source = await after.channel.create_ytdl_player('url')
          # source.start()
        # else:

@bot.command()
async def leave(ctx):
    # Check if the bot is in a voice channel
    print('ctx')

    # Disconnect from the voice channel
    await ctx.voice_client.disconnect()

client.run(TOKEN)