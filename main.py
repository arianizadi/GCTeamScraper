import requests
import json
from bs4 import BeautifulSoup
from lxml import etree

students = dict()
students["gabe"] = "0x1227Db363277DAcf21a8cA0253851EC7b0B8677A"
students["ishan"] = "0xdd21E88EC1EC8657E6D1B845f6d40F1ADa5Ccf50"
students["kyle"] = "0x94fD5E8c7721daF2BdbF0EE01e7A5fF0F8624e12"
students["olivia"] = "0x17Ecd1aCA160cF217edc37acAf45fAce8a6e9769"
students["werner"] = "0x3838728915a96B3F6cF228943749d0fa8FAe9d0c"


def getBalance(url: str) -> int:
    URL = "https://mumbai.polygonscan.com/token/0x3D91462542341ef0BF9dB4b7b828d741E1B41d21?a={}".format(
        url
    )

    page = requests.get(URL)

    balance_xpath = "/html/body/div[1]/main/div[5]/div[2]/div/div/div[2]/text()"
    soup = BeautifulSoup(page.content, "html.parser")
    dom = etree.HTML(str(soup))
    balance = dom.xpath(balance_xpath)
    balance = balance[1].strip()
    balance = balance[0:-10]
    balance = int("".join(filter(str.isdigit, balance)))
    return balance


team_total = 0
for student in students:
    balance = getBalance(students[student])
    team_total += balance
    print("{} has {} tokens".format(student, balance))

print("Team total: {}".format(team_total))
print("Team average: {}".format(team_total / len(students)))
