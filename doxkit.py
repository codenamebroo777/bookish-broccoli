import requests
from bs4 import BeautifulSoup

def get_info_from_411(number):
    url = f"https://www.411.com/phone/{number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    name = soup.find("div", {"class": "name-container"}).text.strip()
    address = soup.find("div", {"class": "address"}).text.strip()
    phone = soup.find("div", {"class": "phone"}).text.strip()
    return {"name": name, "address": address, "phone": phone}

def get_info_from_truepeoplesearch(number):
    url = f"https://www.truepeoplesearch.com/results?phoneno={number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    name = soup.find("span", {"class": "info-section-name"}).text.strip()
    address = soup.find("div", {"class": "info-section-address"}).text.strip()
    phone = soup.find("span", {"class": "info-section-phone"}).text.strip()
    return {"name": name, "address": address, "phone": phone}

def get_info_from_thatsthem(number):
    url = f"https://thatsthem.com/phone/{number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    name = soup.find("div", {"class": "person-name"}).text.strip()
    address = soup.find("div", {"class": "person-address"}).text.strip()
    phone = soup.find("div", {"class": "person-phone"}).text.strip()
    return {"name": name, "address": address, "phone": phone}

def get_info_from_phone_number(number):
    info = {"411": None, "truepeoplesearch": None, "thatsthem": None}
    try:
        info["411"] = get_info_from_411(number)
    except:
        pass
    try:
        info["truepeoplesearch"] = get_info_from_truepeoplesearch(number)
    except:
        pass
    try:
        info["thatsthem"] = get_info_from_thatsthem(number)
    except:
        pass
    return info

