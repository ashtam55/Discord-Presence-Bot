import discord
from discord.ext import commands
client = discord.Client()
client = commands.Bot(command_prefix = '.')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!{round(client.latency*1000)}ms')
        
client.run('Njc4OTQ3ODk0NDc2Mjc1NzI0.XkqNjA.S1HM3yvtAt26Y4qoBQr3YCkqtPU')