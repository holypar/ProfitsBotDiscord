#Import Discord Package
import discord
from discord.ext import commands
import pandas as pd
import bs4
import requests


#Client (the bot)
client = commands.Bot(command_prefix = '$')
@client.command(name = 'version')
async def version(context):

    myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color = 0x5db35d)
    myEmbed.add_field(name = "Version Code", value ="v.1.0.0", inline= False)
    myEmbed.add_field(name="Date Released:", value ="March 13th,2021", inline= False)
    myEmbed.set_footer(text="This is the footer")
    myEmbed.set_author(name ="Par")

    await context.message.channel.send(embed = myEmbed)

@client.command(name = "kick", pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(context,member:discord.Member):
    await member.kick()
    await context.send('User ' + member.display_name + 'has been kicked.')

@client.command(name = "ban", pass_context = True,)
@commands.has_permissions(kick_members = True)
async def ban(context, member: discord.Member, *, reason = None):
    await member.ban(reason= reason)
    await context.send('User ' + member.display_name + 'has been banned.')


@client.event
async def on_ready():
#Do stuff
    general_channel = client.get_channel(717414266487177297)
    await general_channel.send("Let's Get these profits!")
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('with these charts'))

    # df = pd.DataFrame({"A":['Hello', 'Test']})
    # df.to_csv("C:\\Users\pinnd\\OneDrive\\Documents\\ProfitsBotDiscord-1\\Discord Bot\\output.csv")


@client.event
async def on_message(message):
    if message.content == "What is the version?":
            general_channel = client.get_channel(717414266487177297)

            myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color = 0x5db35d)
            myEmbed.add_field(name = "Version Code", value ="v.1.0.0", inline= False)
            myEmbed.add_field(name="Date Released:", value ="March 13th,2021", inline= False)
            myEmbed.set_footer(text="This is the footer")
            myEmbed.set_author(name ="Par")
            await general_channel.send(embed = myEmbed)

    if message.content == "send a DM":
        await  message.author.send("Welcome to Profits Inc!")

    if message.content == "Append":
        #Add a row to my dataframe that contains the message.
        df = pd.read_csv("C:\\Users\pinnd\\OneDrive\\Documents\\ProfitsBotDiscord-1\\Discord Bot\\output.csv",index_col=0)
        df = df.append({"A": 'This is the message I want to append.'},ignore_index=True)
        df.to_csv("C:\\Users\pinnd\\OneDrive\\Documents\\ProfitsBotDiscord-1\\Discord Bot\\output.csv")
            
    await client.process_commands(message)

    if message.author == client.user:
        return   

    if message.content.startswith('pbprice'):
        #general_channel = client.get_channel(717414266487177297)
        #Splitting the input from !price to read input text from user.
        stock = message.content.split(' ')[1]
        url = "https://finance.yahoo.com/quote/"

        full_url = url + stock

        response = requests.get(full_url).content

        soup = bs4.BeautifulSoup(response, 'html.parser')

        stock_price = soup.findAll(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")[0].text

        await message.channel.send(f"The stock price for {stock.upper()} is ${stock_price} currently.")
    
#Run the client on the server
client.run('ODIwMTg3NjcwMjE4NjcwMDgw.YExhSg.4fPa14AfyFIv3CHH1MzqxMzp3UE')

#I made a change
