import requests
from bs4 import BeautifulSoup


class Scraping:
    # params ={
    # "username":"***********",
    # "val":"********************:",
    # "useragent":"",
    # "language":"JAPANESE",
    # }

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.params = {
        "username":self.username,
        "val":self.password,
        "useragent":"",
        "language":"JAPANESE",
        }


    def __session_get(self):
        s = requests.session()
        return s

    def __access(self,s):
        access = s.post("https://el2.y.kumamoto-nct.ac.jp/webclass/login.php?rnd=670fd&mbl=1&language=JAPANESE&mbl=0",
                   data = self.params)

        text = access.text
        mae = "amp;acs_="
        owari = "Name"
        a = text.find(mae)
        b = text.find(owari)
        tmp = text[a+9:b-2]

        return tmp

    def deadline_get(self):
        __access(__session_get())

        re = s.post("https://el2.y.kumamoto-nct.ac.jp//webclass/usr_group_menu.php?rnd=f3dcc&acs_={}".format(tmp))

        page = re.text

        mae = "<head>"
        owari = "</HEAD>"
        a = page.find(mae)
        b = page.find(owari)

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

        return name_list
