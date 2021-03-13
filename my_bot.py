#Import Discord Package
import discord

#Client
client = discord.Client()
@client.event
async def on_ready():
#Do stuff
    general_channel = client.get_channel(717256318347378738)
    await general_channel.send("Hello pussies!")

#Run the client on the server
client.run('ODIwMTg3NjcwMjE4NjcwMDgw.YExhSg.4SxJzWvVtBE8Qoxc9vBs676jdn8')


