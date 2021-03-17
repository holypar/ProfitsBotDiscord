#Import Discord Package
import discord
from discord.ext import commands
import pandas as pd
import bs4
import requests
from yahoo_finance import Share


#Client (the bot)
client = commands.Bot(command_prefix = '$')
@client.command(name = 'version')
async def version(context):

    myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0.1", color = 0x5db35d)
    myEmbed.add_field(name = "Update Log", value ="Can now get stock data by doing pbpr (ticker here)\n\nCan get analyst price targets by doing pbpt (ticker)", inline= False)
    myEmbed.add_field(name="Future Updates", value ="Stock chart support is my main priority at the moment\n\nHosting the bot once shortly after the charting update is finished.", inline= False)
    myEmbed.add_field(name="Date Released:", value ="March 17th,2021", inline= False)
    myEmbed.set_footer(text="Lets get those profits!")
    myEmbed.set_author(name ="Profits Bot")

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

    if message.content.startswith('pbpr'):
        #Splitting the input from !price to read input text from user.
        stock = message.content.split(' ')[1]
        url = "https://finance.yahoo.com/quote/"

        full_url = url + stock

        response = requests.get(full_url).content

        soup = bs4.BeautifulSoup(response, 'html.parser')

        stock_price = soup.findAll(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")[0].text

        await message.channel.send(f"The stock price for {stock.upper()} is ${stock_price} currently.")

    if message.content.startswith('pbpt'):  #price target
        #Splitting the input from !price to read input text from user.
        stock = message.content.split(' ')[1]
        url = "https://money.cnn.com/quote/forecast/forecast.html?symb="

        full_url = url + stock

        response = requests.get(full_url).content

        soup = bs4.BeautifulSoup(response, 'html.parser')

        price_target = soup.findAll(class_ = "wsod_twoCol clearfix")[0].text

        await message.channel.send(price_target)










    # if message.content.startswith('pbchart'):       #pulls up chart
    #     stock = message.content.split(' ')[1]
    #     url = "https://finviz.com/quote.ashx?t="

    #     full_url = url + stock

    #     response = requests.get(full_url).content

    #     soup = bs4.BeautifulSoup(response, 'html.parser')

    #     chart = soup.findAll("img", attrs = {"class" : "chartimg", "id":"chartImgSrc"})



    #not working :(
    # if message.content.startswith('pbstats'):  #tells whether or not to buy a stock on diff timeframes
    #     #Splitting the input from !price to read input text from user.
    #     stock = message.content.split(' ')[1]
    #     url = "https://finance.yahoo.com/chart/"

    #     full_url = url + stock

    #     response = requests.get(full_url).content

    #     soup = bs4.BeautifulSoup(response, 'html.parser')

    #     bullorbear1 = soup.findAll("span")


    #     await message.channel.send(f" {stock.upper()} is\n{bullorbear1} short term\n{bullorbear2} mid term\n{bullorbear3} longterm term")




















    
#Run the client on the server
client.run('ODIwMTg3NjcwMjE4NjcwMDgw.YExhSg.alJFAV9gGk-EGfhdeA3pNG4PQSQ')

#I made a change
