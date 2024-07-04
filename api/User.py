import requests
import urllib.parse

#                                                       
#  88        88   ad88888ba   88888888888  88888888ba   
#  88        88  d8"     "8b  88           88      "8b  
#  88        88  Y8,          88           88      ,8P  
#  88        88  `Y8aaaaa,    88aaaaa      88aaaaaa8P'  
#  88        88    `"""""8b,  88"""""      88""""88'    
#  88        88          `8b  88           88    `8b    
#  Y8a.    .a8P  Y8a     a8P  88           88     `8b   
#   `"Y8888Y"'    "Y88888P"   88888888888  88      `8b  
#                                                       
#
class User:
    def __init__(self):
        self.base_url = "https://api.apacbreachersranked.com/"

    class BreachersUser:
        def __init__(self, id, userName, clanTag, fullUserName):
            self.id = id
            self.userName = userName
            self.clanTag = clanTag
            self.fullUserName = fullUserName

        def __repr__(self):
            return f"<BreachersUser id={self.id}, userName={self.userName}, clanTag={self.clanTag}, fullUserName={self.fullUserName}>"

    def search_users(self, username, json=False):
        '''
        `username` The name of a breachers user\n
        `json` if True return user as json otherwise returns `BreachersUser` object
        '''
        encoded_username = urllib.parse.quote(username)
        result = requests.get(f'{self.base_url}BreachersUser/SearchUsers?SearchString='+encoded_username)
        if result.ok:
            if json:
                return result.json()
            else:
                users = []
                for user in result.json():
                    users.append(self.BreachersUser(**user))
                return users
        else:
            raise ValueError(f"Request error {result.status_code}")

    def get_user(self, BreachersUserId, json=False):
        '''
        `BreachersUserId` The id of a breachers user\n
        `json` if True return user as json otherwise returns `BreachersUser` object
        '''
        encoded_id = urllib.parse.quote(BreachersUserId)
        result = requests.get(f'{self.base_url}BreachersUser/GetUser?BreachersUserId='+encoded_id)
        if result.ok:
            if json:
                return result.json()
            else:
                return self.BreachersUser(**result.json())
        else:
            raise ValueError(f"Request error {result.status_code}")
