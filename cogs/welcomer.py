import discord
from discord.ext import commands


class Welcomer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1140697774950731876)

        embed = discord.Embed(title='Willkommen auf dem Gaming Lounge Discord Server!',
                              description=f'Willkommen {member.mention} auf unserem Server! Wir hoffen du hast Spaß hier!\n\n',
                              color=discord.Color.green())

        embed.set_thumbnail(url=member.avatar_url)

        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Welcomer(bot))