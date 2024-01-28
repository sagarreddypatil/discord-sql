from dotenv import load_dotenv
import os
load_dotenv()

import discord
import sqlite3

con = sqlite3.connect("database.db")

intents = discord.Intents.default()

bot = discord.Bot(intents=intents)


@bot.slash_command()
async def sql(ctx: discord.ApplicationContext, query: str):
    try:
        res = con.execute(query)
        con.commit()
    except Exception as e:
        await ctx.respond(f"Error: {e}")
        return

    out = res.fetchall()
    if len(out) == 0:
        await ctx.respond("Query executed.")
        return

    await ctx.respond("\n".join([str(i) for i in out]))


# To learn how to add descriptions and choices to options, check slash_options.py
bot.run(os.environ["DISCORD_TOKEN"])