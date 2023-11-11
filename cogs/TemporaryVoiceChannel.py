import discord
from discord.ext import commands
from discord.utils import get

class TemporaryVoiceChannel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.temp_channels = []

        @commands.Cog.slash_command(name='setupvoice', description='Setup für Temopary voice')
        @commands.has_permissions(administrator=True)
        async def setup(self, ctx):

            channel = self.bot.get_channel(1152589268695384134)

            embed = discord.Embed(title="Einstellungen der Temporärekanäle",
                                  colour=discord.Colour.green())

            await ctx.respond(embed=embed, components=[
                discord.Button(style=discord.ButtonStyle.green, label="rename", emoji="✍️", custom_id="rename"),
                discord.Button(style=discord.ButtonStyle.red, label="Leave", emoji="🔇", custom_id="leavebutton"),
                discord.Button(style=discord.ButtonStyle.grey, label="Delete", emoji="🗑️", custom_id="delbutton")
                ])

    # Handling button click events
    @commands.Cog.on_click(custom_id='rename')
    async def rename_button(self, ctx, _):
        await ctx.respond("cooming soon", hidden=True)

    @commands.Cog.on_click(custom_id='delbutton')
    async def userinfo_button(self, ctx, _):
        #delete channel
        voice_state = ctx.author.voice

        if voice_state is None:
            # Exiting if the user is not in a voice channel
            embed = discord.Embed(title='You need to be in a temporary voice channel to use this command!',
                                  colour=discord.Colour.red())
            return await ctx.respond(embed=embed, hidden=True)

        if voice_state.channel.id in self.temp_channels:
            self.temp_channels.remove(voice_state.channel.id)
            await voice_state.channel.delete()
            embed = discord.Embed(title='Your voicechannel got deleted!',
                                  colour=discord.Colour.green())
            return await ctx.respond(embed=embed, hidden=True)
        else:
            embed = discord.Embed(title='You need to be in a temporary voice channel to use this command!',
                                  colour=discord.Colour.red())
            return await ctx.respond(embed=embed, hidden=True)


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        name = f"{member.name}´s Channel"

        if hasattr(after.channel, "id"):
            if after.channel.id == 1152589501781258361:
                guild = after.channel.guild
                category = get(guild.categories, id=1152589208163205140)
                channel = await guild.create_voice_channel(category=category, name=name)
                await member.move_to(channel)
                self.temp_channels.append(channel.id)

        if before.channel:
            if before.channel.id in self.temp_channels:
                if len(before.channel.members) == 0:
                    self.temp_channels.remove(before.channel.id)
                    await before.channel.delete()

def setup(bot: commands.Bot):
    bot.add_cog(TemporaryVoiceChannel(bot))
