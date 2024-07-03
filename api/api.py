import requests
import urllib.parse

base_url = "https://api.apacbreachersranked.com/"
#                                            
#    ,ad8888ba,   88888888888  888888888888  
#   d8"'    `"8b  88                88       
#  d8'            88                88       
#  88             88aaaaa           88       
#  88      88888  88"""""           88       
#  Y8,        88  88                88       
#   Y8a.    .a88  88                88       
#    `"Y88888P"   88888888888       88       
#                                            
#                                            

class BreachersUser:
    def __init__(self, id, userName, clanTag, fullUserName):
        self.id = id
        self.userName = userName
        self.clanTag = clanTag
        self.fullUserName = fullUserName

def search_users(username, json=False):
    '''
    `username` The name of a breachers user\n
    `json` if True return user as json otherwise returns `BreachersUser` object
    '''
    encoded_username = urllib.parse.quote(username)
    result = requests.get(f'{base_url}BreachersUser/SearchUsers?SearchString='+encoded_username)
    if result.ok:
        if json:
            return result.json()
        else:
            users = []
            for user in result.json():
                users.append(BreachersUser(**user))
            return users
    else:
        raise ValueError(f"Request error {result.status_code}")

def get_user(BreachersUserId, json=False):
    '''
    `BreachersUserId` The id of a breachers user\n
    `json` if True return user as json otherwise returns `BreachersUser` object
    '''
    encoded_id = urllib.parse.quote(BreachersUserId)
    result = requests.get(f'{base_url}BreachersUser/GetUser?BreachersUserId='+encoded_id)
    if result.ok:
        if json:
            return result.json()
        else:
            return BreachersUser(**result.json())
    else:
        raise ValueError(f"Request error {result.status_code}")

def get_user_match(BreachersUserId, MatchNum, json=False):
    '''
    `BreachersUserId` The id of a breachers user\n
    `MatchNum` the match number you want to get `-1` for all\n
    `json` if True return user as json otherwise returns `BreachersUser` object
    '''
    encoded_id = urllib.parse.quote(BreachersUserId)
    result = requests.get(f'{base_url}MatchStats/CsvMatchData?BreachersPlayerId='+encoded_id)
    if result.ok:
        if json:
            return result.text
        else:
            return BreachersUser(**result.json())
    else:
        raise ValueError(f"Request error {result.status_code}")