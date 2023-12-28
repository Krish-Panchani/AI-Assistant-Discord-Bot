# Copyright 2023 Google LLC & Thunder Develops X Krish Panchani

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import discord
from discord import app_commands
import responses
import re
import config

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#testing command
# @tree.command(name = "krish", description = "My first application Command", guild=discord.Object(id=868378805948022835)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
# async def first_command(interaction):
#     await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    # await tree.sync(guild=discord.Object(id=868378805948022835))
    print("----------------------------------------")
    print(f'AI Assistant Logged in as {client.user}')
    print("----------------------------------------")
    print(f'Bot is Created by Thunder Develops X Krish Panchani (https://www.thunderdevelops.in)')
    print(f'Powered by Vertex AI (https://cloud.google.com/vertex-ai)')
    print("----------------------------------------")
    print("----------------------------------------")
    print(f'Bot is ready to use')
    print("----------------------------------------")

async def send_message(message, user_message):
    try:
        # Generate a response from the model
        response_text = responses.handle_request(user_message)

        await split_and_send_messages(message, response_text, 1700)

     # Send Error Message if something goes wrong   
    except Exception as e:
        print("Error:", e)
                       

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    specific_channel_id = config.channel_id
    # print(str(message.content)) #debugging purpose
    if isinstance(message.channel, discord.TextChannel) and message.channel.id == specific_channel_id:

        #clean the message
        cleaned_text = clean_discord_message(message.content)

        #Start Typing to seem like something happened
        async with message.channel.typing():

            await send_message(message, cleaned_text)


async def split_and_send_messages(message_system, text, max_length):

    # Split the string into parts
    messages = []
    for i in range(0, len(text), max_length):
        sub_message = text[i:i+max_length]
        messages.append(sub_message)

    # Send each part as a separate message
    for string in messages:
        await message_system.channel.send(string)

def clean_discord_message(input_string):
    # Create a regular expression pattern to match text between < and >
    bracket_pattern = re.compile(r'<[^>]+>')
    # Replace text between brackets with an empty string
    cleaned_content = bracket_pattern.sub('', input_string)
    # print(cleaned_content)
    return cleaned_content

client.run(config.discord_bot_token)