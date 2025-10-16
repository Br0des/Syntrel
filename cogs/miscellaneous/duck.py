import discord
from discord.ext import commands
from discord.ext.commands import Context


def duck_command():
    @commands.hybrid_command(
        name="duck",
        description="Duck ASCII art",
    )
    async def duck(self, context):
        duck_art = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟[0;37m⣉⡥⠶⢶⣿⣿⣿⣿⣷⣆[0m⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿[0;37m⢡⡞⠁⠀⠀⠤⠈⠿⠿⠿⠿⣿[0m[0;31m⠀⢻⣦⡈[0m⠻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠘⡁⠀[0;37m⢀⣀⣀⣀⣈⣁⣐⡒[0m[0;31m⠢⢤⡈⠛⢿⡄[0m⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠀[0;37m⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄[0m[0;31m⠉⠐⠄⡈⢀[0m⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠇[0;37m⢠⣿⣿⣿⣿⡿⢿⣿⣿⣿⠁⢈⣿⡄[0m⠀[0;36m⢀⣀[0m⠸⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠟[0;33m⣡⣶⣶⣬⣭⣥⣴[0m[0;37m⠀⣾⣿⣿⣿⣶⣾⣿⣧[0m[0;36m⠀⣼⣿⣷⣌[0m⡻⢿⣿
⣿⣿⠟[0;33m⣋⣴⣾⣿⣿⣿⣿⣿⣿⣿⡇[0m[0;37m⢿⣿⣿⣿⣿⣿⣿⡿[0m[0;36m⢸⣿⣿⣿⣿⣷[0m⠄⢻
⡏[0;33m⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢂[0m[0;37m⣭⣿⣿⣿⣿⣿⠇[0m[0;36m⠘⠛⠛⢉⣉[0m⣠⣴⣾
⣿⣷⣦[0;33m⣬⣍⣉⣉⣛⣛⣉⠉[0m[0;37m⣤⣶⣾⣿⣿⣿⣿⣿⣿⡿[0m⢰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧[0;37m⡘⣿⣿⣿⣿⣿⣿⣿⣿⡇[0m⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇[0;37m⢸⣿⣿⣿⣿⣿⣿⣿⠁[0m⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

        if getattr(context, "interaction", None):
            inter = context.interaction
            if not inter.response.is_done():
                await inter.response.send_message(f"```ansi\n{duck_art}\n```", ephemeral=False)
            else:
                await inter.followup.send(f"```ansi\n{duck_art}\n```", ephemeral=True)
        else:
            await context.send(f"```ansi\n{duck_art}\n```")
    
    return duck
