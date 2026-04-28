import discord
from discord.ext import commands
import requests
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(str(bot.user) + ' has connected to Discord!')

@bot.command(name='linkvertise')
async def bypass_linkvertise(ctx, url: str):
    if 'linkvertise' not in url:
        await ctx.send('This is not a Linkvertise URL.')
        return
    try:
        response = requests.get('https://roles-hours-teaching-ampland.trycloudflare.com/bypass?url=' + url)
        data = response.json()
        if data.get('key'):
            await ctx.send('Bypassed! Key: ' + data['key'])
        elif data.get('result'):
            await ctx.send('Bypassed! Result: ' + data['result'])
        else:
            await ctx.send('Bypass failed. No key returned.')
    except Exception as e:
        await ctx.send('Error: ' + str(e))

bot.run(os.environ['DISCORD_BOT_TOKEN'])
