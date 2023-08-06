# Sellix Discord Bot

This Python Discord bot interacts with Sellix's API to verify customers and assign them a 'Member' role in your Discord server. It also sends notifications to a specific channel whenever a successful sale is made.

## Setup

1. Create a new Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).

2. Invite the bot to your server with the necessary permissions (at least "Read Messages" and "Manage Roles").

3. Obtain your Sellix API key from your Sellix account.

## Installation

Make sure you have Python and `discord.py` installed. You can install `discord.py` using pip:

```pip install discord.py

# Configuration
Replace the following placeholders in the script with your actual values:

'YOUR_DISCORD_BOT_TOKEN': Replace this with your Discord bot token from the Discord Developer Portal.
'YOUR_SELLIX_API_KEY': Replace this with your Sellix API key obtained from your Sellix account.
'YOUR_CHANNEL_ID': Replace this with the ID of the channel where you want to notify admins about sales.
Usage
This bot listens for messages in the server and responds to the command !verify. When a user sends !verify, the bot checks the Sellix API to verify if the user has made a successful sale. If so, it assigns them the 'Member' role and sends a notification to the admin channel specified.

Running the Bot
Simply run the script using the Python interpreter:


```python sellix_discord_bot.py
Note: Make sure your Python environment has the required dependencies installed.
