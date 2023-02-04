"""
██████╗ ██╗  ██╗██╗███████╗██╗   ██╗
██╔══██╗██║  ██║██║██╔════╝╚██╗ ██╔╝
██████╔╝███████║██║███████╗ ╚████╔╝ 
██╔══██╗╚════██║██║╚════██║  ╚██╔╝
██║  ██║     ██║██║███████║   ██║
╚═╝  ╚═╝     ╚═╝╚═╝╚══════╝   ╚═╝   by r4isy#0001 / discord.gg/kenucheck
"""

import discord
from discord.ext import commands, tasks
from discord import Intents

bot = commands.Bot("!", intents=Intents.all())
role_id = "ENTER YOUR ROLE ID"

@tasks.loop(seconds=5)
async def check_activity():
    role = bot.guilds[0].get_role(role_id)
    file = open('role_members.txt', 'r')
    member_list = [str(member.id) for member in bot.get_all_members() if '.gg/kenucheck' in str(member.activity)]
    member_ids = [line[:-1] for line in file.readlines()]
    file.close()
    for member_id in member_ids:
        if member_id not in member_list:
            member = bot.guilds[0].get_member(int(member_id))
            await member.remove_roles(role)
            member_ids.remove(member_id)
    with open('role_members.txt', 'w') as file:
        for member_id in member_ids:
            file.write(member_id + '\n')
    for member_id in member_list:
        if member_id not in member_ids:
            member = bot.guilds[0].get_member(int(member_id))
            await member.add_roles(role)
            with open('role_members.txt', 'a') as file:
                file.write(member_id + '\n')

            
@bot.event
async def on_ready():
    check_activity.start()

bot.run('ENTER YOUR BOT TOKEN')
