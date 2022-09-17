import hikari
import lightbulb
from .spinner.spinner import Spinner

plugin = lightbulb.Plugin("Spinner")
spinner: Spinner = Spinner()

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)

# -- COMMANDS -- 
# ADD
@plugin.command
@lightbulb.option("item", "add an item to the current basket", type=str)
@lightbulb.command("add", "add item to basket")
@lightbulb.implements(lightbulb.SlashCommand)
async def spinner_add(ctx: lightbulb.Context):
    item = ctx.options.item
    spinner.add(item)
    await ctx.respond(f"added item \"{item}\" to basket: {spinner.current_basket}")

# REMOVE
@plugin.command
@lightbulb.option("item", "remove an item from the current basket", type=str)
@lightbulb.command("remove", "remove item from basket")
@lightbulb.implements(lightbulb.SlashCommand)
async def spinner_remove(ctx: lightbulb.Context):
    item = ctx.options.item
    spinner.remove(item)
    await ctx.respond(f"removed item \"{item}\" from the basket: {spinner.current_basket}")

# LIST
@plugin.command
@lightbulb.command("list", "list basket")
@lightbulb.implements(lightbulb.SlashCommand)
async def spinner_list(ctx: lightbulb.Context):
    options = {
        "title": "info",
        "description": spinner.info()
    }

    await ctx.respond(hikari.Embed(**options))

# SPIN
@plugin.command
@lightbulb.command("spin", "spin the wheel")
@lightbulb.implements(lightbulb.SlashCommand)
async def spinner_spin(ctx: lightbulb.Context):
    item = spinner.spin()
    await ctx.respond(f"chosen: {item}")

# CHANGE BASKET
@plugin.command
@lightbulb.option("name", "basket name", type=str)
@lightbulb.command("change", "if basket does not exist, then create a new basket")
@lightbulb.implements(lightbulb.SlashCommand)
async def spinner_change(ctx: lightbulb.Context):
    name = ctx.options.name
    spinner.change_basket(name)
    await ctx.respond(f"in basket: {name}")


# LIST BASKETS
@plugin.command
@lightbulb.command("show", "list all baskets")
@lightbulb.implements(lightbulb.SlashCommand)
async def spinner_list(ctx: lightbulb.Context):
    options = {
        "title": spinner.info_basket()
    }

    await ctx.respond(hikari.Embed(**options))

# REMOVE BASKET
@plugin.command
@lightbulb.option("name", "basket name", type=str)
@lightbulb.command("delete", "delete basket")
@lightbulb.implements(lightbulb.SlashCommand)
async def spinner_change(ctx: lightbulb.Context):
    name = ctx.options.name
    spinner.remove_basket(name)
    await ctx.respond(f"removed basket: {name}")

# COIN FLIP
@plugin.command
@lightbulb.command("flip", "simple coin flip")
@lightbulb.implements(lightbulb.SlashCommand)
async def spinner_change(ctx: lightbulb.Context):
    choice = spinner.coin()
    await ctx.respond(hikari.Embed(title=choice))   
