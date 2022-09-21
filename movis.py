import requests # API -> input [movie name] -> output [movie info]
import discord 
from discord.ext import commands
needed_intents = discord.Intents.all()
bot = commands.Bot(command_prefix=',',intents=needed_intents)

@bot.command()
async def movie(ctx, *, arg):
  data = requests.get(f'https://api.themoviedb.org/3/search/multi?api_key=e44beea2db1e5054940ae762ef1d9d66&query={arg}&page=1')
  print(data.json()['results'][0])
  movie = data.json()['results'][0]
  if movie['media_type'] == "movie":
    embed=discord.Embed(title=movie['original_title'], description=movie['overview'], color=0x8a8a8a)
    embed.add_field(name="Release Date", value=movie['release_date'], inline=True)
  else:
    embed=discord.Embed(title=movie['name'], description=movie['overview'], color=0x8a8a8a)
    embed.add_field(name="Release Date", value=movie['first_air_date'], inline=True)

  # embed.set_author(name=ctx.author.name, icon_url=ctx.message.author.avatar_url)
  embed.set_image(url=f"https://www.themoviedb.org/t/p/w600_and_h900_bestv2{movie['poster_path']}")
  
  embed.add_field(name="Rating", value=movie['vote_average'])
  embed.add_field(name="Type", value=movie['media_type'])
  await ctx.send(embed=embed)
  # await ctx.send("error")

@bot.event
async def on_ready():
  print("what up")
bot.run('MTAyMjExNzg1NTEyNDI3OTMyNg.GUHJ-4.yjT5MhuPv-Ao3Q9CjNe8KbZtDoc5dP2Sqlaj2A')