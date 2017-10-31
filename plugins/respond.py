from slackbot.bot import respond_to
import ../scraping


s = requests.session()

@respond_to('3BC締め切り')
@respond_to('3MI締め切り')
def deadline(message,s):
    username = "bc5366imam"
    password = "******************"
    scraping_insrance = Scraping(username,password)

    name_list = scraping_insrance.deadline()
    for messagee in name_list:
        message.reply(messagee)

    message.reply('締め切りはないYO')
