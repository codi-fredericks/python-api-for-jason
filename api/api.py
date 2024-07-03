import requests
import urllib.parse

base_url = "https://api.apacbreachersranked.com/"
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

#                                                                                                    
#  88b           d88         db    888888888888  ,ad8888ba,   88        88  88888888888  ad88888ba   
#  888b         d888        d88b        88      d8"'    `"8b  88        88  88          d8"     "8b  
#  88`8b       d8'88       d8'`8b       88     d8'            88        88  88          Y8,          
#  88 `8b     d8' 88      d8'  `8b      88     88             88aaaaaaaa88  88aaaaa     `Y8aaaaa,    
#  88  `8b   d8'  88     d8YaaaaY8b     88     88             88""""""""88  88"""""       `"""""8b,  
#  88   `8b d8'   88    d8""""""""8b    88     Y8,            88        88  88                  `8b  
#  88    `888'    88   d8'        `8b   88      Y8a.    .a8P  88        88  88          Y8a     a8P  
#  88     `8'     88  d8'          `8b  88       `"Y8888Y"'   88        88  88888888888  "Y88888P"   
#                                                                                                    
#                                                                                                    

class Match():
    def __init__(self, id, players, timestamp, game_data):
        self.id = id
        self.players = players
        self.timestamp = timestamp #UTC
        self.game_data = self.MatchData(**game_data)
    
    class MatchData():
        def __init__(self, MapName, matchMode ,matchType, players, playersLeft, allPlayers):
            self.MapName = MapName
            self.matchMode = matchMode
            self.matchType = matchType
            self.players = []
            for player in players:
                self.players.append(self.MatchPlayer(**player))
            self.playersLeft = []
            for player in playersLeft:
                self.playersLeft.append(self.MatchPlayer(**player))
            self.allPlayers = []
            for player in allPlayers:
                self.allPlayers.append(self.MatchPlayer(**player))
        
        class MatchPlayer():
            def __init__(self, ApiId, clanTag, GameMatchDataResult, score, gameTimeInSeconds, gameTime, mvp, penaltyReason, rounds, timeAfk, Username):
                self.ApiId = ApiId
                self.clanTag = clanTag
                self.GameMatchDataResult = GameMatchDataResult
                self.score = score
                self.gameTimeInSeconds = gameTimeInSeconds
                self.gameTime = gameTime
                self.mvp = mvp
                self.penaltyReason = penaltyReason
                self.rounds = []
                for round in rounds:
                    self.rounds.append(self.MatchPlayerRound(**round))
                self.timeAfk = timeAfk
                self.Username = Username
            
            class MatchPlayerRound():
                def __init__(self, ace, assists, botAssists, deaths, firstBlood, mvp, roundNumber, roundTime, team, teamWon, gadgets, weapons):
                    self.ace = ace
                    self.assists = assists
                    self.botAssists = botAssists
                    self.deaths = deaths
                    self.firstBlood = firstBlood
                    self.mvp = mvp
                    self.roundNumber = roundNumber
                    self.roundTime = roundTime
                    self.team = team
                    self.teamWon = teamWon
                    self.gadgets = []
                    for gadget in gadgets:
                        self.gadgets.append(Gadget(**gadget))
                    self.weapons = []
                    for weapon in weapons:
                        self.weapons.append(Weapon(**weapon))

def get_user_match(BreachersUserId, json=False):
    '''
    `BreachersUserId` The id of a breachers user\n
    `MatchNum` the match number (0-9) you want to get `-1` for all matches\n
    `json` if True return user as json otherwise returns `BreachersUser` object
    '''
    encoded_id = urllib.parse.quote(BreachersUserId)
    result = requests.get(f'{base_url}BreachersApi/get_match_data?player_id='+encoded_id)
    print(result.status_code)
    if result.ok:
        if json:
            return result.json()
        else:
            matches = []
            for i in result.json():
                matches.append(Match(**i))
            return matches
    else:
        raise ValueError(f"Request error {result.status_code}")
    



class Gadget():
    def __init__(self, Name, botDamageDone, botKills, damageDone, destroyed, enemyTriggered, friendlyDamageDone, kills, teamHealed, triggered, used):
        self.Name = Name
        self.botDamageDone = botDamageDone
        self.botKills = botKills
        self.damageDone = damageDone
        self.destroyed = destroyed
        self.enemyTriggered = enemyTriggered
        self.friendlyDamageDone = friendlyDamageDone
        self.kills = kills
        self.teamHealed = teamHealed
        self.triggered = triggered
        self.used = used

class Weapon():
    def __init__(self, Name, botDamageDone, botHeadshotKills, botKills, damageDone, friendlyDamageDone, headshotKills, shotsFired, totalHeadshots, totalKills, totalShotsHit):
        self.Name = Name
        self.botDamageDone = botDamageDone
        self.botHeadshotKills = botHeadshotKills
        self.botKills = botKills
        self.damageDone = damageDone
        self.friendlyDamageDone = friendlyDamageDone
        self.headshotKills = headshotKills
        self.shotsFired = shotsFired
        self.totalHeadshots = totalHeadshots
        self.totalKills = totalKills
        self.totalShotsHit = totalShotsHit