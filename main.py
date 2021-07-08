import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()

bot_prefix = ttk.Entry()
bot_token = ttk.Entry()
number_of_commands = ttk.Entry()
bot_playing_message = ttk.Entry()

root.title("discord.py bot template")

#the gui portion of the program
ttk.Label(text="type in the prefix of the bot").grid(row=0,column=0,columnspan=3)
bot_prefix.grid(row=1,column=0,columnspan=3)

ttk.Label(text="type in the token of the bot").grid(row=2,column=0,columnspan=3)
bot_token.grid(row=3,column=0,columnspan=3)

ttk.Label(text="type in the number of commands for the bot").grid(row=4,column=0,columnspan=3)
number_of_commands.grid(row=5,column=0,columnspan=3)

ttk.Label(text="type in the 'currently playing game' message for the bot").grid(row=6,column=0,columnspan=3)
bot_playing_message.grid(row=7,column=0,columnspan=3)

#generates template and writes it to txt
def gen():

    global bot_prefix
    global bot_token
    global number_of_commands
    global bot_playing_message

    prefix = bot_prefix.get()
    token = bot_token.get()
    nmrcmds = number_of_commands.get()
    msg = bot_playing_message.get()

    #erases file
    open("bot_template_result.txt", "w").close()
    
    botscript = open("bot_template_result.txt", "a")
    botscript.write("""import discord
from discord.ext import commands
    
bot_token = {}
client = commands.Bot(command_prefix = "{}")

""".format(token, prefix))

    for x in range(int(nmrcmds)):

        botscript.write("""@client.command()
async def command{}(ctx):
    pass

""".format(x))

    botscript.write("""@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("{}"))

client.run(bot_token)""".format(msg))

    botscript.close()
    messagebox.showinfo("Success!", "Your discord.py template has been successfuly made and you can close the window. The tempalate can be found in 'bot_template_result.txt' which is located in the current folder")

sbmt = ttk.Button(text="Submit", command=gen)
sbmt.grid(row=8,column=0,columnspan=3)

root.mainloop()
