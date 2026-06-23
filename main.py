import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
import math
import random
import requests
import time


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

spamming = False


@bot.command()
async def start(ctx):
    global spamming
    spamming = True

    while spamming:
        payload = {
            'content': "name: Qrezn \n Looking for bunny ears, upgrading I have 40k\n click to send a trade send ANYTHING i will A/C: https://www.roblox.com/users/136106879/trade \n https://media.discordapp.net/attachments/442709710408515605/1518432847671591062/image.png?ex=6a39e64a&is=6a3894ca&hm=d9d3c65ca7cbf0312800c8a777144bcbdc5b077a541dda9c5dcd89ab842b745f&=&format=webp&quality=lossless&width=459&height=312 "
        } 

        header = {
            'authorization': "NzA3NTQ1MDExMTY3ODIxODM2.G8K9nm._ubFxAttT452BXat2hg_gxEeCjCG7f_0lC_hEE"
        }
        r = requests.post("https://discord.com/api/v9/channels/812908225405255703/messages",

        data=payload, headers=header)
        
        await asyncio.sleep(random.randint(1, 10))


@bot.command()
async def stop(ctx):
    global spamming
    spamming = False
    await ctx.send("Stopped.")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run("MTUxODcxMTk1Nzg5NTY0MzI0OA.GEn7xn.kz57gkQ4XrzQAuzaCHJN7UM0idfmN9DTD6z1d0")
