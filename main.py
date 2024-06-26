import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


#BAN COMMAND
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason= "No reason"):
    try:
        await user.ban(reason=reason)
        embed = discord.Embed(color=discord.Color.red(), title="", description="")
        embed.add_field(name="Banned:", value=f"""
The user **{user}** has been banned.
Reason = **{reason}**
""", inline=True)
        ctx.reply(embed=embed)
    except:
            embed = discord.Embed(color=discord.Color.red(), title="", description="")
            embed.add_field(name="Banned:", value=f"""
Error 
""", inline=True)         

#KICK COMMAND
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason= "No reason"):
    try:
        await user.kick(reason=reason)
        embed = discord.Embed(color=discord.Color.red(), title="", description="")
        embed.add_field(name="Kicked:", value=f"""
The user **{user}** has been kicked.
Reason = **{reason}**
""", inline=True)
        ctx.reply(embed=embed)
    except:
            embed = discord.Embed(color=discord.Color.red(), title="", description="")
            embed.add_field(name="kicked:", value=f"""
Error 
""", inline=True)   

bot.run("")
