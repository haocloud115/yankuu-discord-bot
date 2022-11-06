import discord
from itertools import cycle
import time
from discord.ext import commands, tasks

import youtube_dl 
from youtube_dl import YoutubeDL
class Music(commands.Cog):
    def __init__(self,client):
        self.client = client
        
        self.is_playing = False
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}
        self.vc = ""

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}    
    
    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True


            m_url = self.music_queue[0][0]['source']


            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    

    @commands.command(name="play", help="Phát nhạc trên youtube")
    async def p(self, ctx, *args):
        query = " ".join(args)
        try:
          voice_channel = ctx.author.voice.channel
        except:
            await ctx.send("Bạn phải vào một kênh thoại để sử dụng !")
            return
        song = self.search_yt(query)
        if type(song) == type(True):
          await ctx.send("Không thể tải bài hát xuống ! Note : Sử dụng link stream hoặc list bài hát sẽ không sử dụng được")
        else:
          await ctx.send(f"Bài hát đã được thêm vào bởi {ctx.author}")
          self.music_queue.append([song, voice_channel])
          if self.is_playing == False:
            await self.play_music()



    @commands.command(name="queue", help="Thêm bài hát vào hàng chờ")
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"
        if retval != "":
            await ctx.send(f"**{retval}**")
        else:
            await ctx.send("Không có bài hát nào trong hàng chờ")

    @commands.command(name="skip", help="Sờ kíp bài hát")
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            await self.play_music()

    @commands.command(name="stop", help="Tắt nhạc")
    async def stop(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            self.is_playing = False

    @commands.command(name = "pause", help = "Dừng bài đang phát")
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        
        await ctx.send("Đã dừng !")

    @commands.command(name = "resume", help = "Tiếp tục bài hát")
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Đã tiếp tục.")
    
    @commands.command(name = "leave", help = "Rời khỏi voice")
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command(name = "join", help = "Tham gia voice")
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Bạn có ở trong voice đâu")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

def setup(client):
    client.add_cog(Music(client))