import hikari
import lightbulb
from .dreidel_spinner.dreidel import Dreidel

dreidel_plugin = lightbulb.Plugin("Dreidel")
dreidel: Dreidel = Dreidel()

def load(bot: lightbulb.BotApp):
    bot.add_plugin(dreidel_plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(dreidel_plugin)

# -- COMMANDS -- 
# SPIN
@dreidel_plugin.command
@lightbulb.command("dspin", "spin the dreidel")
@lightbulb.implements(lightbulb.SlashCommand)
async def dreidel_spin(ctx: lightbulb.Context):
    random_dreidel_face_data = dreidel.spin()

    dreidel_face_name = random_dreidel_face_data["face_name"]
    dreidel_face_meaning = random_dreidel_face_data["meaning"]
    
    await ctx.respond(f"{dreidel_face_name}!\n{dreidel_face_meaning}")
