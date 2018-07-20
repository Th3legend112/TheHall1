# welcome-bot
# import all necessary commands and libraries
import discord
import asyncio

client=discord.Client()
@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name +" joined")
    newUserMessage = """**Welcome to The Hall :house: """   + member.name +   """ please make sure to read the rules and enjoy your stay
The Hall is a community based server centred around providing a fun and relaxed environment for its users.
-We have :**
```diff
- Custom Bots , NSFW content , Games , Active Members , Partner and Hypesquad Discord Members , Giveaways , Music , Ranking System  and more...``` """

    await client.send_message(member, newUserMessage)
    await client.send_message(discord.Object(id='453679995357888522'), ':house:  |_**Hello ('+member.name+') :wave:  Welcome to the Hall, have fun!**_')
    print("Sent message to " + member.name)


client.run('NDY5NjAzMTU3NTA5NjY4ODY0.DjLP6g.AORkb3xerZT3uc1WshPcPz-cDew')
