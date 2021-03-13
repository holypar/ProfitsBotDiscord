#Import Discord Package
import discord

#Client
client = discord.Client()
@client.event
async def on_ready():
#Do stuff
    general_channel = client.get_channel(717414266487177297)
    await general_channel.send("Let's Get these profits!")

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

#Run the client on the server
client.run('ODIwMTg3NjcwMjE4NjcwMDgw.YExhSg.w-nvq4YE6DqWnkLIhhSy5sKX1Dg')

#I made a change
