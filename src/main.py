import os
import hikari 
import lightbulb
from plugins.spinner_plugin.spinner_plugin import plugin

from dotenv import load_dotenv
load_dotenv()

bot = lightbulb.BotApp(token=os.getenv("DISCORD_TOKEN"), default_enabled_guilds=(837504788391919677))

@bot.listen(hikari.StartedEvent)
async def on_started(event):    
    print("Bot is ready!")

bot.add_plugin(plugin)
bot.run()