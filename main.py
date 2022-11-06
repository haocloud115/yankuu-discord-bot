import discord
import aiohttp
import pyfiglet
import random
import os
import json
import io
import re
import contextlib
import textwrap
from discord import user
from requests import PreparedRequest
import session
import requests
import datetime
import asyncio
# import keep_alive
from discord_slash import SlashContext
from discord_slash.utils import manage_commands
from discord_slash import SlashCommand
from itertools import cycle
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands.core import has_permissions
import random
from discord.ext.commands import has_permissions, CheckFailure, check
import time
import aiofiles

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='yk.', help_command=None)
bot = commands.Bot(command_prefix='yk.', help_command=None)
slash = SlashCommand(client, sync_commands=True)


## slash command
@slash.slash(name="ping", description="Độ chậm của bot")
async def _ping(ctx: SlashContext):
    before = time.monotonic()
    msg = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000.
    await msg.edit(
        content=f"Pong ! **{int(ping)}**ms <:wifi:1030119132613586954>")


@slash.slash(name="help", description="Sử dụng cái này để hiểu thêm về bot")
async def _help(ctx: SlashContext):
    em = discord.Embed(
        title=
        "<:6776moderatorsimplified:1030052145740906517> Lệnh help của YanKuu",
        description="Sử dụng yk.help <lệnh> để có thêm chi tiết")
    em.add_field(
        name="Fun",
        value=
        f"<:9002anyasly:1030052149356396584> yk.help fun để biết thêm chi tiết"
    )
    em.add_field(
        name="Moderation",
        value=
        "<:6776moderatorsimplified:1030052145740906517> yk.help mod để biết thêm chi tiết"
    )
    em.add_field(
        name="Utility",
        value=
        "<:4a07bbdf6f9c4317a100e9796a4edd1b:1030052143379513384> yk.help utility để biết thêm chi tiết"
    )
    em.add_field(
        name="NSFW",
        value=
        "<:pngclipartlasciviousbehaviorgfyc:1030052810554867754> yk.help nsfw để biết thêm chi tiết"
    )
    em.add_field(
        name="Music",
        value=
        "<:doesntneedmoneymokoudiscordemoji:1030052152741208074> yk.help music để biết thêm chi tiết."
    )
    em.set_image(
        url=
        'https://i.pinimg.com/originals/f3/bf/85/f3bf85ec59620ba85cf2a6a5e0245571.gif'
    )
    await ctx.send(embed=em)
    print(f'help slash is used by {ctx.author.id}')


@slash.slash(name="invite", description="Invite Bot")
async def _invite(ctx: SlashContext):
    em = discord.Embed(
        title="Click để invite bot",
        url=
        "https://discord.com/oauth2/authorize?client_id=1030333902742630530&permissions=8&scope=bot%20applications.commands",
        color=discord.Color(0xffff))
    em.add_field(
        name="YanKuu Team:",
        value=
        "<:happy:1030349666858057799> Cảm ơn bạn đã sử dụng bot! Team Dev sẽ làm việt hết sức để đem đến trải nghiệm tốt nhất!!!"
    )
    em.set_image(
        url=
        'https://pa1.narvii.com/5848/fd5c202e98624e005dbcf09a5874adf99a0925e3_hq.gif'
    )

    await ctx.reply(embed=em)
    print(f'invite slash is used by {ctx.author.id}')


@slash.slash(name="problem", description="Báo Cáo Sự Cố!!!")
async def _problem(ctx: SlashContext):
    em = discord.Embed(title="Thắc mắc về các lệnh hay có vấn đề về bot?",
                       url="https://discord.gg/vmaKKM3jJU",
                       color=discord.Color(0xffff))
    em.add_field(
        name="YanKuu Team:",
        value=
        "Bot owner online discord thường xuyên nên bạn có thể thoải mái báo cáo nha!!!"
    )
    em.set_image(
        url=
        'https://i.pinimg.com/originals/98/94/f7/9894f73861f84b4965f5a910de032567.gif'
    )

    await ctx.reply(embed=em)
    print(f'problem slash is used by {ctx.author.id}')


@slash.slash(name="botinfo", description="Thông Tin Về Bot")
async def _botinfo(ctx: SlashContext):
    em = discord.Embed(title=f"Info của bot!", colour=ctx.author.colour)
    em.add_field(name="Ngày được tạo ra:", value="<t:1640789220:R>")
    em.add_field(name="Developer:", value="HaoCloud#0024")
    em.add_field(name="Commands:", value="61 Lệnh")
    em.add_field(name="Số lệnh slash: ", value="5")
    em.set_footer(
        text="Support server : https://discord.gg/vmaKKM3jJU - Made by HaoCloud"
    )
    em.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/1030120472509173810/1030381421992345600/unknown.png"
    )
    em.set_image(
        url=
        "https://steamuserimages-a.akamaihd.net/ugc/967606226459507315/8D1BB25BD1708F49C5053D0E03644918A547ADC3/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"
    )
    await ctx.reply(embed=em)
    print(f'bot info slash is used by {ctx.author.id}')


#-------------------------------------------------------------------------------------------------#

#===== LỆNH CHO BOT


#help -----
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="<:verify:1030123703234740255> Lệnh help của YanKuu",
        description="Sử dụng yk.help <lệnh> để biết thêm chi tiết")
    em.add_field(name="Fun <:9002anyasly:1030052149356396584>",
                 value=f"yk.help fun ")
    em.add_field(
        name="Moderation <:6776moderatorsimplified:1030052145740906517>",
        value="yk.help mod")
    em.add_field(
        name="Utility <:4a07bbdf6f9c4317a100e9796a4edd1b:1030052143379513384>",
        value="yk.help utility để biết thêm chi tiết")
    em.add_field(
        name="NSFW <:pngclipartlasciviousbehaviorgfyc:1030052810554867754>",
        value="yk.help nsfw để biết thêm chi tiết")
    em.add_field(
        name="Music <:doesntneedmoneymokoudiscordemoji:1030052152741208074>",
        value="yk.help music để biết thêm chi tiết.")
    em.set_image(
        url=
        'https://i.pinimg.com/originals/f3/bf/85/f3bf85ec59620ba85cf2a6a5e0245571.gif'
    )
    await ctx.send(embed=em)
    print(f'help is used by {ctx.author.id}')


@help.command()
async def mod(ctx):
    mod = discord.Embed(
        title="<:spaceman:1030117218102558721> **Mod Command!**",
        description=
        "YanKuu sẽ giúp bạn quản lý server nhanh hơn khi dùng những lệnh này",
        colour=ctx.author.colour)
    mod.add_field(
        name="MOD",
        value=
        "snipe - clear - nuke - (un)mute - (un)ban - warn - warnings - kick - botinfo - role - renamevc - renamesv"
    )
    mod.set_image(url='https://media.tenor.com/FS6nlZVkHrIAAAAC/yandere.gif')
    await ctx.send(embed=mod)


@help.command()
async def music(ctx):
    music = discord.Embed(
        title="<:837244412492513312:1030338392006869002> **Music Command!**",
        description="Notes: Music chỉ là bản demo nên còn có nhiều lỗi",
        color=0xffff)
    music.add_field(name="MUSIC",
                    value="play - stop - join - leave - queue - skip")
    music.set_image(
        url=
        'https://steamuserimages-a.akamaihd.net/ugc/912423178600997332/6C965D544521C988FC3CA241B46E4EE272C45DAD/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false'
    )
    await ctx.send(embed=music)


@help.command()
async def fun(ctx):
    fun = discord.Embed(
        title="<:4419anyasmug:1030336786054000701> **Fun Command!**",
        description="Chơi đùa cùng YanKuu ~~",
        colour=ctx.author.colour)
    fun.add_field(
        name="FUN",
        value=
        "waifu - naycacchau - fbi - neko - coinflip - bang - pat - hug - leuleu - cry - blush - lick - kiss - slap - kill - wink - punch - smug - poke - bite - dance - wait - meme - gayrate - simprate - trueordare - ship"
    )
    fun.set_image(url='https://i.gifer.com/FAPk.gif')
    await ctx.send(embed=fun)


@help.command()
async def utility(ctx):
    utility = discord.Embed(
        title="<:9435blurplebot:1030339644769976380> **Utility Module!**",
        description="Những lệnh khác của bot AkiNio !",
        colour=ctx.author.colour)
    utility.add_field(
        name="UTILITY",
        value=
        "av - serverinfo - whois - botinfo - quotes - ping - rd - invite - report - say"
    )
    utility.set_image(
        url=
        'https://i.pinimg.com/originals/3d/8c/75/3d8c75e93917c8ed6f3980e49939d009.gif'
    )
    utility.set_footer(text="Notes: Các lệnh đang được update!!!")
    await ctx.reply(embed=utility)


@help.command()
async def nsfw(ctx):
    nsfw = discord.Embed(title="NSFW !",
                         description="~~ YanKuu có chút dam dang đó nha",
                         color=0xffff)
    nsfw.add_field(name="Onii-chan hentai:",
                   value="porn - hentai - hneko - bucu - fuck - hloli - bb")
    nsfw.set_image(
        url=
        'https://cdn.myanimelist.net/s/common/uploaded_files/1449716038-3e0e04d04201b5f53d496753dc283001.gif'
    )
    await ctx.reply(embed=nsfw)

@client.command()
async def dev(ctx):
    nsfw = discord.Embed(title="DEV DEF",
                         description="~~ Gửi info vào console",
                         color=0xffff)
    nsfw.add_field(name="Các lệnh hiện tại",
                   value="howmanyserver - addpremiumuser - removepremiumuser - apremiumcommand")
    nsfw.set_image(
        url=
        'https://cdn.myanimelist.net/s/common/uploaded_files/1449716038-3e0e04d04201b5f53d496753dc283001.gif'
    )
    await ctx.reply(embed=nsfw)


#============================
#moderation commands:
@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content,
                                                message.author,
                                                message.channel.name,
                                                message.created_at)


async def timeout_user(*, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {client.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() +
               datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with client.session.patch(url, json=json,
                                    headers=headers) as session:
        if session.status in range(200, 299):
            return True
        return False


@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[
            ctx.guild.id]

    except:
        await ctx.channel.send("Không có tin nhắn để snipe!")
        return

    embed = discord.Embed(description=contents,
                          color=discord.Color.purple(),
                          timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}",
                     icon_url=author.avatar_url)
    embed.set_footer(text=f"Xóa tại : #{channel_name}")

    await ctx.channel.send(embed=embed)


@client.command()
async def ping(ctx):
    before = time.monotonic()
    msg = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000.
    await msg.edit(content=f"Ping này : {int(ping)}ms")


@client.command(aliases=["purge"])
@commands.has_permissions(manage_channels=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount + 1)
    print(f'clear is used by {ctx.author}')


@client.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None:
        await ctx.send("Bạn phải mention một kênh !")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Đã được nuke!")
        await nuke_channel.delete()
        await new_channel.send(
            f"Đã nuke kênh. Người dùng lệnh: **{ctx.author.mention}**")
        await ctx.send("Nuke kênh thành công!")

    else:
        await ctx.send(f"Không tìm thấy kênh **{channel.name}**")


@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False,
                                          read_message_history=True,
                                          read_messages=False)
    embed = discord.Embed(title="Muted",
                          description=f"{member.mention} đã bị mute",
                          colour=discord.Colour.light_gray())
    embed.add_field(name="Lí do:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"Bạn đã bị mute ở **{guild.name}** vì : **{reason}**")


@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title="Unmuted",
                          description=f"{member.mention} đã được unmute !",
                          colour=discord.Colour.light_gray())
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'Ðã khóa kênh ! bởi {ctx.author.mention}')


@client.command()
@has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,
                                      send_messages=True)
    await ctx.send(ctx.channel.mention +
                   f" **đã được unlock bởi : {ctx.author.mention}**")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'Ðã cấm {member.mention}')
    except:
        await ctx.send(f'Không thể ban{member.mention}')


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Hãy nhập dúng lí do hoặc người bị ban!")


@client.command(name='unban')
async def unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.channel.send(f'{user.mention} đã được unban!')
    await ctx.guild.unban(user)


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Hãy nhập ID người được unban !")


def is_it_me(ctx):
    return ctx.author.id == ctx.author.id


client.warnings = {}


@client.event
async def on_ready():
    for guild in client.guilds:
        client.warnings[guild.id] = {}

        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append(
                        (admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [
                        1, [(admin_id, reason)]
                    ]


@client.event
async def on_guild_join(guild):
    client.warnings[guild.id] = {}


def owner(ctx):
    return ctx.author.id == 926777498312798258


@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member = None, *, reason=None):
    if member is None:
        return await ctx.send("Không tìm thấy người bạn muốn cảnh cáo!")

    if reason is None:
        return await ctx.send("Hãy nhập lí do để cảnh cáo người này.")

    try:
        first_warning = False
        client.warnings[ctx.guild.id][member.id][0] += 1
        client.warnings[ctx.guild.id][member.id][1].append(
            (ctx.author.id, reason))

    except KeyError:
        first_warning = True
        client.warnings[ctx.guild.id][member.id] = [
            1, [(ctx.author.id, reason)]
        ]

    count = client.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(
        f"{member.mention} có {count} {'cảnh cáo' if first_warning else 'cảnh cáo'}."
    )


@client.command()
@commands.has_permissions(manage_messages=True)
async def warnings(ctx, member: discord.Member = None):
    if member is None:
        return await ctx.send("Không thể tìm thấy người bạn muốn xem cảnh cáo")

    embed = discord.Embed(title=f"Số lần cảnh cáo của {member.name}",
                          description="",
                          colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Cảnh cáo {i}** bởi: {admin.mention} vì: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError:  # no warnings
        await ctx.send("Người này không có cảnh cáo nào cả.")


@client.command()
async def afk(ctx, mins):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} đã afk với lí do là : **{mins}**.")
    await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} không còn afk nữa !")
            break


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=None)
        await ctx.send(f'Thành viên {member} đã bị kick')
    except:
        await ctx.send("Không thể kick thành viên đó!")


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


#Utility commands
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.command()
async def quotes(ctx):
    quote = get_quote()
    await ctx.send(quote)


# ascii - ping
@client.command(aliases=['av'])
async def avatar(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    em = discord.Embed(title=str(member), color=0xffff)
    em.set_image(url=member.avatar_url)
    await ctx.reply(embed=em, mention_author=False)


@client.command()
async def botinfo(ctx):
    em = discord.Embed(title=f"Info của bot!", colour=ctx.author.colour)
    em.add_field(name="Ngày được tạo ra:", value="<t:1640789220:R>")
    em.add_field(name="Developer:", value="HaoCloud#0024")
    em.add_field(name="Commands:", value="61 Lệnh")
    em.add_field(name="Số lệnh slash: ", value="4")
    em.set_footer(
        text="Support server : https://discord.gg/vmaKKM3jJU - Made by HaoCloud"
    )
    em.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/1030120472509173810/1030381421992345600/unknown.png"
    )
    em.set_image(
        url=
        "https://steamuserimages-a.akamaihd.net/ugc/967606226459507315/8D1BB25BD1708F49C5053D0E03644918A547ADC3/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"
    )
    await ctx.reply(embed=em)


@client.command(pass_context=True)
async def setnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname đã được đổi cho {member.mention}')


format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


@client.command(aliases=['svi'])
@commands.guild_only()
async def serverinfo(ctx):
    embed = discord.Embed(color=ctx.author.color)
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    embed.add_field(
        name=f"Thông tin về **{ctx.guild.name}**: ",
        value=
        f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Chủ: **{ctx.guild.owner}** \n:white_small_square: Vùng: **{ctx.guild.region}** \n:white_small_square: Ngày tạo: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Thành viên: **{ctx.guild.member_count}** \n:white_small_square: Các kênh: **{channels}** kênh; **{text_channels}** kênh văn bản, **{voice_channels}** kênh thoại, **{categories}** số danh mục \n:white_small_square: Mức độ bảo mật: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Tình năng: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}"
    )
    await ctx.send(embed=embed)


def cog_check(self, ctx):
    return ctx.author.id == 984113692025167902


@client.command(aliases=["eval"])
async def e(self, ctx, *, code: str = None):
    if code is None:
        return await ctx.send("Ghi code vào lmao thằng ngu")

    code = code.lstrip("```python").rstrip("\n```").lstrip("\n")

    local_vars = {
        "discord": discord,
        "commands": commands,
        "client": self.client,
        "ctx": ctx,
    }
    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(f"async def func():\n{textwrap.indent(code, '    ')}",
                 local_vars)

            obj = await local_vars["func"]()
            result = f"{stdout.getvalue()}"

    except Exception as e:
        result = e

    if len(str(result)) >= 2000:
        result = result[:1900]
        await ctx.send("Kết quả lớn hơn 2000 ký tự"
                       "Điền số kí tự nhỏ hơn 2000 đi.")

    await ctx.send(f"```python\n{result}```")


@client.command('role')
@commands.has_permissions(administrator=True)  #permissions
async def role(ctx, user: discord.Member, *, role: discord.Role):
    if role.position > ctx.author.top_role.position:  #if the role is above users top role it sends error
        return await ctx.send(
            '**❌ | Vai trò đó cao hơn vai trò trên cùng của bạn!**')
    if role in user.roles:
        await user.remove_roles(role)  #removes the role if user already has
        await ctx.send(f"Đã gỡ {role} khỏi {user.mention}")
    else:
        await user.add_roles(role)  #adds role if not already has it
        await ctx.send(f"Đã thêm {role} cho {user.mention}")


@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(),
                          timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Yêu cầu bởi {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Tên:", value=member.display_name)

    embed.add_field(
        name="Tài khoản được tạo vào:",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="Tham gia server từ :",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Vai trò:",
                    value="".join([role.mention for role in roles]))
    embed.add_field(name="Vai trò trên cùng:", value=member.top_role.mention)
    print(member.top_role.mention)
    embed.set_footer(text=f"Yêu cầu bởi {ctx.author}")
    await ctx.send(embed=embed)


@client.command(aliases=["iv"])
async def invite(ctx):
    em = discord.Embed(
        title="Click để invite bot",
        url=
        "https://discord.com/oauth2/authorize?client_id=1030333902742630530&permissions=8&scope=bot%20applications.commands",
        color=discord.Color(0xffff))
    em.add_field(
        name="YanKuu Team:",
        value=
        "<:happy:1030349666858057799> Cảm ơn bạn đã sử dụng bot! Team Dev sẽ làm việt hết sức để đem đến trải nghiệm tốt nhất!!!"
    )
    em.set_image(
        url=
        'https://pa1.narvii.com/5848/fd5c202e98624e005dbcf09a5874adf99a0925e3_hq.gif'
    )

    await ctx.reply(embed=em)


@client.command(aliases=["pb", "report"])
async def problem(ctx):
    em = discord.Embed(title="Thắc mắc về các lệnh hay có vấn đề về bot?",
                       url="https://discord.gg/vmaKKM3jJU",
                       color=discord.Color(0xffff))
    em.add_field(
        name="YanKuu Team:",
        value=
        "Bot owner online discord thường xuyên nên bạn có thể thoải mái báo cáo nha!!!"
    )
    em.set_image(
        url=
        'https://i.pinimg.com/originals/98/94/f7/9894f73861f84b4965f5a910de032567.gif'
    )

    await ctx.reply(embed=em)
    print(f'problem is used by {ctx.author.id}')


@client.command(aliases=["random"])
async def rd(ctx, *, args=None):
    if args == None:
        rd = random.randint(1, 10000000)
        await ctx.send(
            "<a:rikka:932095702660706305> | **Bạn được chọn số:** " + str(rd))
    else:
        rd2 = random.randint(1, int(args))
        await ctx.send(
            "<a:rikka:932095702660706305> | **Số mà tôi chọn nàyyy:** " +
            str(rd2))


#Fun Command=========
@client.command()
@commands.guild_only()
async def waifu(ctx):
    r = requests.get("https://api.waifu.pics/sfw/waifu")
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title=f"Ảnh waifu của bạn đây")
    embed.set_image(url=ulr)
    embed.set_footer(text="By HaoCloud")
    await ctx.send(embed=embed)


@client.command()
async def naycacchau(ctx):
    embed = discord.Embed(title="Này các cháu, ông hỏi!!!")
    embed.set_image(url="https://i.makeagif.com/media/9-02-2019/hWevJ1.gif")
    embed.set_footer(text=f"{ctx.author} hư quá")
    await ctx.reply(embed=embed)


@client.command()
async def fbi(ctx):
    fbi = discord.Embed(title="FBI OPEN UP!!!", color=0xffff)
    fbi.set_image(
        url="https://media3.giphy.com/media/jmSjPi6soIoQCFwaXJ/200.gif")
    fbi.set_footer(text="Made by HaoCloud")
    await ctx.reply(embed=fbi)


@client.command(name="neko")
@commands.guild_only()
async def neko(ctx):
    q = [f"https://api.waifu.pics/sfw/neko"]
    s = random.choice(q)
    r = requests.get(s)
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title=f"Ảnh neko của bạn đây")
    embed.set_image(url=ulr)
    embed.set_footer(text="By HaoCloud")
    await ctx.send(embed=embed)


@client.command(aliases=['cf'])
async def coinflip(ctx):
    choicezz = [
        '**Ngửa** nhé <:coinngua:1030419201439043595> !',
        '**Sấp** nhá <:coinsap:1030419206673535056> !!'
    ]
    await ctx.send(random.choice(choicezz))


@client.command()
async def bang(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2

        ulr = 'https://i.pinimg.com/originals/39/4d/00/394d00e713d6b3a4a928651deaccdfc0.gif'
        embed = discord.Embed(title=f"{ctx.author} đã bắn {user_1}",
                              color=0xffff)
        embed.set_image(url=ulr)
        embed.set_footer(text=f"By HaoCloud")
        await ctx.reply(embed=embed)


@client.command()
async def pat(ctx,
              user_1: discord.Member = None,
              user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2
        r = requests.get("https://api.waifu.pics/sfw/pat")
        r = r.json()
        ulr = r['url']
        embed = discord.Embed(title=f"{ctx.author} đang xoa đầu {user_1} :DD",
                              color=0xffff)
        embed.set_image(url=ulr)
        embed.set_footer(text="By HaoCloud")
        await ctx.reply(embed=embed)


@client.command()
async def hug(ctx,
              user_1: discord.Member = None,
              user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2
        r = requests.get("https://api.waifu.pics/sfw/hug")
        r = r.json()
        ulr = r['url']
        embed = discord.Embed(title=f"{user_1} vừa bị {ctx.author} ôm <3",
                              color=0xffff)
        embed.set_image(url=ulr)
        embed.set_footer(text="By HaoCloud")
        await ctx.reply(embed=embed)


@client.command()
async def leuleu(ctx):
    em = discord.Embed(title="Lêu lêu", color=0xffff)
    em.set_image(
        url=
        "https://media.discordapp.net/attachments/927713935044513804/927776209977376798/Frog_Tongue_Out_Sticker_-_Frog_Tongue_Out_Teasing_-_Discover__Share_GIFs.gif?width=431&height=431"
    )
    await ctx.reply(embed=em)


@client.command()
async def cry(ctx):
    r = requests.get("https://api.waifu.pics/sfw/cry")
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title=f"{ctx.author} đang khóc :'(", color=0xffff)
    embed.set_image(url=ulr)
    embed.set_footer(text="By HaoCloud")
    await ctx.reply(embed=embed)


@client.command()
async def blush(ctx):
    r = requests.get("https://api.waifu.pics/sfw/blush")
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title=f"{ctx.author} đang đỏ mặt kìa ><",
                          color=0xffff)
    embed.set_image(url=ulr)
    embed.set_footer(text="Made by HaoCloud")
    await ctx.reply(embed=embed)


@client.command()
async def lick(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2

        r = requests.get("https://api.waifu.pics/sfw/lick")
        r = r.json()
        ulr = r['url']
        embed = discord.Embed(title=f"{user_1} đã bị {ctx.author} liếm :3",
                              color=0xffff)
        embed.set_image(url=ulr)
        embed.set_footer(text="By HaoCloud")
        await ctx.reply(embed=embed)


@client.command()
async def kiss(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2

        r = requests.get("https://api.waifu.pics/sfw/kiss")
        r = r.json()
        ulr = r['url']
        embed = discord.Embed(title=f"{user_1} dã bị {ctx.author} hôn <3",
                              color=0xffff)
        embed.set_image(url=ulr)
        embed.set_footer(text="By HaoCloud")
        await ctx.reply(embed=embed)


@client.command()
async def slap(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2

        r = requests.get("https://api.waifu.pics/sfw/slap")
        r = r.json()
        ulr = r['url']
        embed = discord.Embed(title=f"{user_1} đã bị tát bởi {ctx.author} :o",
                              color=0xffff)
        embed.set_image(url=ulr)
        embed.set_footer(text="By HaoCloud")
        await ctx.reply(embed=embed)


@client.command()
async def kill(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1

        if not user_2 == None:
            user = user_1
            users = user_2

        r = requests.get("https://api.waifu.pics/sfw/kill")
        r = r.json()
        ulr = r['url']
        aki = discord.Embed(title=f"{ctx.author} vừa giết {user_1} !")
        aki.set_image(url=ulr)
        aki.set_footer(text="By HaoCloud")
        await ctx.reply(embed=aki)


@client.command()
async def wink(ctx):
    #quên
    r = requests.get("https://api.waifu.pics/sfw/wink")
    r = r.json()
    ulr = r['url']
    aki = discord.Embed(title=f"{ctx.author} đang nháy mắt :?", color=0xffff)
    aki.set_image(url=ulr)
    aki.set_footer(text="By HaoCloud")
    await ctx.reply(embed=aki)


@client.command()
async def punch(ctx,
                user_1: discord.Member = None,
                user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:

            r = requests.get("https://api.waifu.pics/sfw/bully")
            r = r.json()
            ulr = r['url']
            kimi = discord.Embed(
                title=f"{user_1} đang bị {ctx.author} ăn hiếp ;-;",
                color=0xffff)
            kimi.set_image(url=ulr)
            kimi.set_footer(text="Made by HaoCloud")
            await ctx.reply(embed=kimi)


@client.command()
async def smug(ctx):
    r = requests.get("https://api.waifu.pics/sfw/smug")
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title=f"{ctx.author} đang **nhếch mép**",
                          color=0xffff)
    embed.set_image(url=ulr)
    embed.set_footer(text="By HaoCloud")
    await ctx.reply(embed=embed)


@client.command()
async def poke(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2
    r = requests.get("https://api.waifu.pics/sfw/poke")
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title=f"{ctx.author} đang chọc {user_1} !!")
    embed.set_image(url=ulr)
    embed.set_footer(text="By HaoCloud")
    await ctx.reply(embed=embed)


@client.command()
async def bite(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2

    r = requests.get("https://api.waifu.pics/sfw/bite")
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title=f"{ctx.author} đang cắn {user_1} ÒwÓ")
    embed.set_image(url=ulr)
    embed.set_footer(text="By HaoCloud")
    await ctx.reply(embed=embed)


@client.command()
async def dance(ctx):

    r = requests.get("https://api.waifu.pics/sfw/dance")
    r = r.json()
    ulr = r['url']
    em = discord.Embed(title=f"{ctx.author} đang múa ÙwÚ", color=0xffff)
    em.set_image(url=ulr)
    em.set_footer(text="By HaoCloud")
    await ctx.reply(embed=em)


@client.command()
async def wait(ctx):
    em = discord.Embed(title=f"{ctx.author} đang chờ đợi :p", color=0xffff)
    em.set_image(
        url=
        "https://cdn.discordapp.com/attachments/921395702721040415/927838296128757800/loli-anime.gif"
    )
    await ctx.reply(embed=em)


@client.command(pass_context=True)
async def meme(ctx):
    cak = discord.Embed(title="Meme đây!", color=0xffff)

    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                'https://www.reddit.com/r/Animemes/new.json?sort=hot') as r:
            res = await r.json()
            cak.set_image(url=res['data']['children'][random.randint(0, 25)]
                          ['data']['url'])
            await ctx.send(embed=cak)


@client.command()
async def gayrate(ctx, member: discord.Member = None):
    gay = random.randint(1, 100)
    if member == None:
        gayrate = ctx.author
        embed = discord.Embed(
            title="Gay-rate Machine",
            description=f":rainbow_flag: {gayrate} bị gay {gay}%")
    else:
        embed = discord.Embed(
            title="Gay-rate Machine",
            description=f":rainbow_flag: {member.mention} bị gay {gay}% ")
    await ctx.send(embed=embed)


@client.command()
async def simprate(ctx, member: discord.Member = None):
    simp = random.randint(1, 100)
    if member == None:
        simprate = ctx.author
        embed = discord.Embed(
            title="Simp-rate Machine",
            description=
            f"<:spaceman:1030117218102558721> {simprate} bị simp {simp}%")
    else:
        embed = discord.Embed(
            title="Simp-rate Machine",
            description=
            f"<:spaceman:1030117218102558721> {member.mention} bị simp {simp}%"
        )
    await ctx.send(embed=embed)


@client.command(aliases=['tod'])
async def trueordare(ctx):
    true = [
        "<:LuxiriaTenshi_Heart:1030116642132336660> ÒwÓ **sự thật** nhé",
        "<:LuxiriaTenshi_Heart:1030116642132336660> UwU **thử thách** đó"
    ]
    await ctx.send(random.choice(true))


@client.command()
@commands.guild_only()
async def ship(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = None):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2
        arg = random.randint(1, 100)
        r = requests.get("https://api.waifu.pics/sfw/hug")
        r = r.json()
        ulr = r['url']

        embed = discord.Embed(
            title=f"Tình cảm mà {user} dành cho {users} là {arg}% ❤️")
        embed.set_image(url=ulr)

        await ctx.channel.send(embed=embed)
    if users == None:
        users = ctx.author


@client.command(name='membercount')
async def membercount(ctx):
    memberCount = str(ctx.guild.member_count)

    embed = discord.Embed(title=f"Số lượng thành viên tại {ctx.guild.name}",
                          description=f"{memberCount} thành viên",
                          color=0xffff)
    embed.set_footer(text=f"Người dùng lệnh: {ctx.author}")
    await ctx.send(embed=embed)


#gaws command #gaws = giveaways

time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}


def convert(argument):
    args = argument.lower()
    matches = re.findall(time_regex, args)
    time = 0
    for key, value in matches:
        try:
            time += time_dict[value] * float(key)
        except KeyError:
            raise commands.BadArgument(
                f"{value} Cần phải là thời gian hợp lệ ! Ví dụ như : 10s|10m|10h|10d"
            )
        except ValueError:
            raise commands.BadArgument(f"{key} Không hợp lệ")
    return round(time)


@client.command()
@commands.has_permissions(manage_messages=True)
async def gstart(ctx, timing, winners: int, *, prize):
    await ctx.send('Giveaway đã bắt đầu', delete_after=3)
    gwembed = discord.Embed(
        title=
        "<:pepega:1030355627874205786> **Giveaway** <:pepega:1030355627874205786>",
        description=f'Giải thưởng: **{prize}**',
        color=0xb4e0fc)
    gwembed.add_field(name="React <:ga:1030355247811534881> để tham gia !",
                      value="React đi react đi !!! <:ga:1030355247811534881>")
    time = convert(timing)
    gwembed.set_footer(
        text=f"Kết thúc vào {time} giây nữa | Tổ chức bởi {ctx.author}")
    gwembed = await ctx.send(embed=gwembed)
    await gwembed.add_reaction("<:ga:1030355247811534881>")
    await asyncio.sleep(time)
    message = await ctx.fetch_message(gwembed.id)
    users = await message.reactions[0].users().flatten()
    users.pop(users.index(ctx.guild.me))
    if len(users) == 0:
        await ctx.send("Không có người thắng cuộc.")
        return
    for i in range(winners):
        winner = random.choice(users)
        await ctx.send(
            f"Chúc mừng {winner.mention} đã thắng **{prize}** || Tổ chức bởi {ctx.author.mention}!"
        )


#=============
#NFSW COMMAND
@client.command()
@commands.is_nsfw()
async def porn(ctx):
    embed = discord.Embed(title="Nót sếp pho wuôrk", color=0xffff)
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                'https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]
                            ['data']['url'])
            await ctx.send(embed=embed)


@porn.error
async def porn_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send(
            f"Người dùng: {ctx.author.mention}! Lệnh này chỉ được sử dụng trong kênh NSFW!!!"
        )


@client.command(name="hentai")
@commands.guild_only()
@commands.is_nsfw()
async def hentai(ctx):
    q = ["https://api.waifu.pics/nsfw/waifu"]
    s = random.choice(q)
    r = requests.get(s)
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title=f"Ảnh hentai của bạn đây >~<")
    embed.set_image(url=ulr)
    embed.set_footer(text="By HaoCloud")
    await ctx.send(embed=embed)


@hentai.error
async def hentai_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send(
            f"Người dùng: {ctx.author.mention}! Lệnh này chỉ được sử dụng trong kênh NSFW!!!"
        )


@client.command()
@commands.is_nsfw()
async def bb(ctx):
    embed = discord.Embed(title="Ngực nè bú đi", color=0xffff)
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                'https://www.reddit.com/r/BigAnimeTiddies/new.json?sort=hot'
        ) as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]
                            ['data']['url'])
            embed.set_footer(text="Made by HaoCloud")
            await ctx.send(embed=embed)


@bb.error
async def bb_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send(
            f"Người dùng: {ctx.author.mention}! Lệnh này chỉ được sử dụng trong kênh NSFW!!!"
        )


@client.command()
@commands.is_nsfw()
async def hloli(ctx):
    choicess = [
        'https://static.hentai-gif-anime.com/upload/20171111/40/81835/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81834/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81832/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81833/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81831/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81830/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81829/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81828/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81826/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81825/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81824/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81821/thumbnail.gif',
        'https://static.hentai-gif-anime.com/upload/20171111/40/81822/thumbnail.gif',
        'https://i.makeagif.com/media/9-02-2019/hWevJ1.gif'
    ]
    loli = discord.Embed(title="Cẩn thận fbi nhá", color=0xffff)
    loli.set_image(url=f"{random.choice(choicess)}")
    loli.set_footer(text="By HaoCloud")

    await ctx.reply(embed=loli)


@hloli.error
async def loli_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        fbi = discord.Embed(
            title=
            f"Người dùng: {ctx.author.mention}! Lệnh này chỉ được sử dụng trong kênh NSFW!!!"
        )
        fbi.set_image(
            url="https://media.giphy.com/media/3o6wNPIj7WBQcJCReE/giphy.gif")
        fbi.set_footer(text=f"?? {ctx.author}")
        await ctx.send(embed=fbi)


###################################################################################################


# Code hentai
@client.command(aliases=['codehentai'])
@commands.is_nsfw()
async def nhentai(ctx):
    code = [
        "167466",
        "165684",
        "254048",
        "175015",
        "174016",
        "142825",
        "129128",
        "171417",
        "129128",
        "95809",
        "239567",
        "247021",
        "46579",
        "123580",
        "171417",
        "173543",
        "197422",
        "187835",
        "217832",
        "206573",
        "169546",
        "193107",
        "190805",
        "220309",
        "211112",
        "132768",
        "97945",
        "164783",
        "206446",
        "251608",
        "90182",
        "256018",
        "138470",
        "110826",
        "175494",
        "134764",
        "145647",
        "212562",
        "179166",
        "214784",
        "176977",
        "191434",
        "191434",
        "239536",
        "236342",
        "227702",
        "204425",
        "205079",
        "85333",
        "232837",
        "232385",
        "232341",
        "254087",
        "50535",
        "235202",
        "94159",
        "52365",
        "255034",
        "153045",
        "159457",
        "173235",
        "96270",
        "196020",
        "191774",
        "230332",
        "95298",
        "89514",
        "73649",
        "203027",
        "217404",
        "65573",
        "255457",
        "199874",
        "233133",
        "205367"
        "233693",
        "50046",
        "234191",
        "209455",
        "206366",
        "253799",
        "39249",
        "172197",
        "243552",
        "223998",
        "221050",
        "217456",
        "225019",
        "234165",
        "258245",
        "247696",
        "258212",
        "258465",
        "86493",
        "258133",
        "244327",
        "260640",
        "261171",
        "244996",
        "202634",
        "165950",
        "220967",
        "120977",
        "204746",
        "142850",
        "99439",
        "232439",
        "246032",
        "200948",
        "265804",
        "25913",
        "262861",
        "196077",
        "155489",
        "257528",
        "267270",
        "177044",
        "267502",
        "184840",
        "144714",
        "228575",
        "268002",
        "267980",
        "227439",
        "267980",
        "268015",
        "89502",
        "228575",
        "220893",
        "160609",
        "261107",
        "110747",
        "235532",
        "248196",
        "228948",
        "259361",
        "235032",
        "139512",
        "257528",
        "260369",
        "261650",
        "234174",
        "116174",
        "249554",
        "249551",
        "249543",
        "49544",
        "166427",
        "206295",
        "168574",
        "249497",
        "72987",
        "181008",
        "242987",
        "251019",
        "251008",
        "251007",
        "185572",
        "69431",
        "187626",
        "251014",
        "251015",
        "251027",
        "251028",
        "251029",
        "251024",
        "251026",
        "239732",
        "213835",
        "146913",
        "216227",
        "182290",
        "117013",
        "259600",
        "139512",
        "258479",
        "173101",
        "235532",
        "258488",
        "264551",
        "263661",
        "242668",
        "154884",
        "150096",
        "265842",
        "259137",
        "781573",
        "234734",
        "244436",
        "265841",
        "265837",
        "255337",
        "110955",
        "265842",
        "266301",
        "928040",
        "122557",
        "135420",
        "209519",
        "265756",
        "136489",
        "242517",
        "266965",
        "134035",
        "266613",
        "183469",
        "244996",
        "255662",
        "267352",
        "267270",
        "267043",
        "213560",
        "261868",
        "267352",
        "186938",
        "267369",
        "263516",
        "266942",
        "111292",
        "233513",
        "262069",
        "172807",
        "263960",
        "184840",
        "266495",
        "252548",
        "267617",
        "193770",
        "262668",
        "225918",
        "147759",
        "154290",
        "240108",
        "240110",
        "208486",
        "240113",
        "257960",
        "109168",
        "109395",
        "109519",
        "112206",
        "231215",
        "246186",
        "267980",
        "259491",
        "265933",
        "196016",
        "235032",
        "228948",
        "131056",
        "121927",
        "134861",
        "195791",
        "116300",
        "268362",
        "152889",
        "134500",
        "268338",
        "220735",
        "192060",
        "113276",
        "265526",
        "264824",
        "126784",
        "191851",
        "103366",
        "229144",
        "158651",
        "257484",
        "248696",
        "265804",
        "206387",
        "158123",
        "136188",
        "235928",
        "194941",
        "208797",
        "241819",
        "239732",
        "215376",
        "220212",
        "165957",
        "266906",
        "268529",
        "267352",
        "229144",
        "253687",
        "238577",
    ]

    await ctx.send(
        f"<:pngclipartlasciviousbehaviorgfyc:1030052810554867754> | code của bạn đây: {random.choice(code)}"
    )


###################################################################################################


# BUCU
@client.command(aliases=['blowjob'])
@commands.is_nsfw()
async def bucu(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2

        r = requests.get("https://api.waifu.pics/nsfw/blowjob")
        r = r.json()
        ulr = r['url']
        embed = discord.Embed(
            title=f"{ctx.author} đang buscu {user_1}, thật là lãng mạn <3",
            color=0xffff)
        embed.set_image(url=ulr)
        embed.set_footer(text="By HaoCloud")
        await ctx.reply(embed=embed)


@bucu.error
async def bucu_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.reply(
            f"Người dùng: {ctx.author.mention}! Lệnh này chỉ được sử dụng trong kênh NSFW!!!"
        )


###################################################################################################

#hneko


@client.command(name="hneko")
@commands.guild_only()
@commands.is_nsfw()
async def hneko(ctx):
    q = ["https://api.waifu.pics/nsfw/neko"]
    s = random.choice(q)
    r = requests.get(s)
    r = r.json()
    ulr = r['url']
    embed = discord.Embed(title="Ảnh neko hentai của bạn dây")
    embed.set_footer(text="By HaoCloud")
    embed.set_image(url=ulr)
    await ctx.send(embed=embed)


@hneko.error
async def hneko_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.reply(
            f"Người dùng: {ctx.author.mention}! Lệnh này chỉ được sử dụng trong kênh NSFW!!!"
        )


###################################################################################################


# Fuck
@client.command()
@commands.is_nsfw()
async def fuck(ctx,
               user_1: discord.Member = None,
               user_2: discord.Member = discord.Member):
    if not user_1 == None:
        if user_2 == None:
            user = ctx.author
            users = user_1
        if not user_2 == None:
            user = user_1
            users = user_2
        choicesss = [
            'https://cdn.discordapp.com/attachments/736281485216317442/736281794927919164/fuck.gif',
            'https://cdn.discordapp.com/attachments/736281485216317442/736281509488754740/fuck.gif',
            'https://cdn.sex.com/images/pinporn/2013/07/21/3238759.gif?width=620',
            'https://images-ext-1.discordapp.net/external/NOpUdEv4ojFdpQPfB-yOijj_DZ59LKe6yU2QcFpbzMM/http/xxxpicz.com/xxx/gifs-hentai-porno-hentai-vidahentaiporn-1.gif?width=400&height=234'
        ]

        embed = discord.Embed(title=f"{ctx.author} dã djt {user_1} :o")
        embed.set_image(url=f"{random.choice(choicesss)}")
        embed.set_footer(text="Made by HaoCloud")
        await ctx.reply(embed=embed)


@fuck.error
async def fuck_error(ctx, error):
    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.reply(
            f"Người dùng: {ctx.author.mention}! Lệnh này chỉ được sử dụng trong kênh NSFW!!!"
        )


###################################################################################################

client.sniped_messages = {}
status = cycle(['YanKuu', 'https://discord.gg/vmaKKM3jJU'])


# Ready Console
@client.event
async def on_ready():
    print(f'{client.user} suc vat nhat the gioi')
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(
        activity=discord.Streaming(name=f'yk.help || {servers} servers',
                                   url='https://www.twitch.tv/discord'))


###################################################################################################

# LOG SERVER



@client.event
async def on_guild_join(guild):

    bot_count = len([b for b in guild.members if b.bot])
    bot_count = len([b for b in guild.members if b.bot])
    print(f'Add to {guild.name} with id: {guild.id}')
    embed = discord.Embed(
        title=f"Bot đã được add",
        description=(f"Bot đã được add vào **{guild.name}**!"),
        color=0xffff).add_field(
            name="ID", value=guild.id, inline=False).add_field(
                name="Số thành viên",
                value=f"+{guild.member_count}",
                inline=False).add_field(
                    name="Phần trăm bot sang user",
                    value=f"{round(bot_count / guild.member_count * 100, 2)}%",
                    inline=False)

    await client.get_channel(1030351840656769086).send(embed=embed)



@client.event
async def on_guild_remove(guild):

    bot_count = len([b for b in guild.members if b.bot])
    print(f'Remove from {guild.name} with id: {guild.id}')
    embed = discord.Embed(
        title="Bot đã được loại bỏ",
        description=f"YanKuu vừa bị kick khỏi **{guild.name}**",
        color=0xffff).add_field(
            name="ID", value=guild.id, inline=False).add_field(
                name="Số thành viên",
                value=f"-{guild.member_count}",
                inline=False).add_field(
                    name="Phần trăm bot sang user",
                    value=f"{round(bot_count / guild.member_count * 100, 2)}%",
                    inline=False)

    await client.get_channel(1030351840656769086).send(embed=embed)


###################################################################################################

# Command Error


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="**__ Thiếu Giá Trị !!!__**",
                              description="Hãy điền thêm gì đó ở sau lệnh.",
                              color=0x000000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed1 = discord.Embed(
            title="**__?Bạn thiếu quyền hạn cần thiết?__**",
            description="Bạn thiếu quyền hạn cần thiết để sử dụng lệnh này.",
            color=0x000000)
        await ctx.send(embed=embed1)
    if isinstance(error, commands.BotMissingPermissions):
        embed4 = discord.Embed(
            title="**__?Bot thiếu quyền hạn cần thiết?__**",
            description=
            "Bot thiếu quyền hạn, hãy cho bot role cao hơn hoặc re-invite bot để fix cái này",
            color=0x000000)
        await ctx.send(embed=embed4)
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="**__Lệnh không tìm thấy__**",
            description=f"\n```\n Lệnh mà bạn vừa nhập không tồn tại. \n```\n",
            color=0x000000)
        await ctx.send(embed=embed)

        return
    raise error


for filename in os.listdir('./cogs'):
    if (filename.endswith('.py')):
        client.load_extension(f'cogs.{filename[:-3]}')

###################################################################################################

#premium user


@client.command()
async def addpremiumuser(ctx, user: discord.Member):
    if ctx.author.id != 984113692025167902:  #put your user id on discord here
        return

    with open("premium_users.json") as f:
        premium_users_list = json.load(f)

    if user.id not in premium_users_list:
        premium_users_list.append(user.id)

    with open("premium_users.json", "w+") as f:
        json.dump(premium_users_list, f)

    await ctx.send(f"{user.mention} has been added!")


@client.command()
async def removepremiumuser(ctx, user: discord.Member):
    if ctx.author.id != 984113692025167902:  #put your user id on discord here
        return

    with open("premium_users.json") as f:
        premium_users_list = json.load(f)

    if user.id in premium_users_list:
        premium_users_list.remove(user.id)
    else:
        await ctx.send(
            f"{user.mention} is not in the list, so they cannot be removed!")
        return

    with open("premium_users.json", "w+") as f:
        json.dump(premium_users_list, f)

    await ctx.send(f"{user.mention} has been removed!")


def check_if_user_has_premium(ctx):
    with open("premium_users.json") as f:
        premium_users_list = json.load(f)
        if ctx.author.id not in premium_users_list:
            return False

    return True


@client.command()
@check(check_if_user_has_premium)
async def apremiumcommand(ctx):
    await ctx.send("Hello premium user!")


@apremiumcommand.error
async def apremiumcommand_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry, but you are not a premium user!")
    else:
        raise error


##############################

## SAY


@client.command()
async def say(ctx, *args):
    arguments = ' '.join(args)
    await ctx.send(f'{arguments}')
    await ctx.message.delete()



# HOW MANY SERVER


@client.command()
async def howmanyserver(ctx):
    servers = len(client.guilds)
    embed = discord.Embed(title=":white_check_mark: Successful",
                          desc="Successfully Send To Console")
    await ctx.send(embed=embed)
    print(
        f'{ctx.author.name} use server command. YanKuu has been adding to {servers} server'
    )

#### test


# keep_alive.keep_alive()
try:
    client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
