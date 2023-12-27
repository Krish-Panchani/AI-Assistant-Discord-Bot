import discord
from discord import app_commands
import responses

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#testing command
@tree.command(name = "krish", description = "My first application Command", guild=discord.Object(id=1181160674529918986)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1181160674529918986))
    print("Ready!")

async def send_message(message, user_message):
    try:
        response = responses.handle_request(user_message)
        # response = vertex_ai.gen_response(user_message)
        await message.channel.send(response)
        
    except Exception as e:
        print("Error:", e)
                       

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # username = str(message.author)
    user_message = str(message.content)
    # channel = str(message.channel.name)

    await send_message(message, user_message)

        
client.run("YOUR DISCORD BOT TOKEN")