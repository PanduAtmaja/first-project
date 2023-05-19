import discord

# Variabel intents menyimpan hak istimewa bot
Intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
Intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(Intents=Intents)


@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTEwMzk4MTc3MDA0MDQxODMxNQ.GiiHW9.0V1130NWAyhBbKWS6Siea2XvKXi2Lz-IavuHao")
