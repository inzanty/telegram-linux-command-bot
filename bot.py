import json
import subprocess
import telebot

configFile = open('config.json')
config = json.load(configFile)
bot = telebot.TeleBot(config["token"])

# Get argument from command and convert from list to string
def extract_arg(arg):
    string = ""
    return string.join(arg.split()[1:])

@bot.message_handler(commands=['command'])
def exec_command(message):
    argument = extract_arg(message.text)
    if argument != "":
        try:
            command_response = subprocess.Popen(argument, shell=False, stdout=subprocess.PIPE).stdout.read()
            bot.reply_to(message, command_response)
        except FileNotFoundError as error:
            bot.reply_to(message, error)
    else:
        bot.reply_to(message, "Command argument is empty")

bot.polling()
