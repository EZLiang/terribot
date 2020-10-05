import discord, sys

client = discord.Client()


@client.event
async def on_ready():
    global ban
    print('Terribot is now online!')
    for role in client.guilds[0].roles:
        if role.name == "nominally banned":
            ban = role


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "cookie hexagon salad" in message.content:
        await message.author.add_roles(ban)
        await message.channel.send("OK " + ban.mention)


def main():
    client.run(sys.argv[1])


if __name__ == '__main__':
    main()