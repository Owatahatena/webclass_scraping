from slackbot.bot import respond_to

@respond_to('3BC締め切り')
@respond_to('3MI締め切り')
def deadline(message):
    import requests

    params ={
    "username":"***********",
    "val":"********************:",
    "useragent":"",
    "language":"JAPANESE",
    }

    s = requests.session()
    access = s.post("https://el2.y.kumamoto-nct.ac.jp/webclass/login.php?rnd=670fd&mbl=1&language=JAPANESE&mbl=0",
               data = params)

    text = access.text
    mae = "amp;acs_="
    owari = "Name"
    a = text.find(mae)
    b = text.find(owari)
    #print(a)
    #print(text[a+9:b-2])
    tmp = text[a+9:b-2]

    re = s.post("https://el2.y.kumamoto-nct.ac.jp//webclass/usr_group_menu.php?rnd=f3dcc&acs_={}".format(tmp))
    #print(re.text)

    page = re.text

    mae = "<head>"
    owari = "</HEAD>"
    a = page.find(mae)
    b = page.find(owari)

    #print(page[b:])

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page[b:],"html.parser")

    deadline_list = []
    for td in soup.find_all("td"):
        a = td.find('a')
        deadline_list.append(a)

    name_list = []
    for i in deadline_list:
        i = str(i)
        if i.find("red_moji") > 0:
            mae = i.find("»")
            ato = i.rfind("»")
            name = i[mae+2:ato-29]
            name_list.append(name)

    for messagee in name_list:
        message.reply(messagee)

    message.reply('締め切りはないYO')
