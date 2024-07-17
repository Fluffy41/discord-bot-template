import logging
from dotenv import load_dotenv
import os
import discord

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

#intents = discord.Intents.all()  # Enables all intents for the bot, granting it full access to all events and data.

# Alternatively, if you want to enable specific intents manually, here's how you can do it:
intents = discord.Intents.default()  # Starts with the default set of intents (recommended for most bots).

#intents.guilds = True  # Enables intent for guild-related events.
#intents.members = True  # Enables intent for guild member-related events, such as join, leave, update.
#intents.bans = True  # Enables intent for ban and unban events.
#intents.emojis = True  # Enables intent for emoji update events.
#intents.integrations = True  # Enables intent for integration update events.
#intents.webhooks = True  # Enables intent for webhook update events.
#intents.invites = True  # Enables intent for invite update events.
#intents.voice_states = True  # Enables intent for voice state update events, important for voice-related features.
#intents.presences = True  # Enables intent for tracking user presences (status, game playing, etc.).
#intents.messages = True  # Enables intent for message events, including creating, updating, and deleting.
#intents.guild_messages = True  # Enables intent for guild message events specifically.
#intents.dm_messages = True  # Enables intent for direct message events.
#intents.reactions = True  # Enables intent for reaction add, remove, clear events on messages.
#intents.guild_reactions = True  # Enables intent for guild message reactions specifically.
#intents.dm_reactions = True  # Enables intent for direct message reactions.
#intents.typing = True  # Enables intent for typing start events, can be used to show typing indicators.
#intents.guild_typing = True  # Enables intent for guild typing events specifically.
#intents.dm_typing = True  # Enables intent for direct message typing events.

# Note: Enabling all intents, especially the privileged ones (members and presences), requires verification and explicit enabling in the Discord developer portal.

print(intents)

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    logging.info(f'{client.user} has connected to Discord!')
    print(f'{client.user} has connected to Discord!')


client.run(os.getenv("DISCORD_TOKEN"))
