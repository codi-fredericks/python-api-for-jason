import requests
import urllib.parse


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


class Matches():
    def __init__(self):
        self.base_url = "https://api.apacbreachersranked.com/"

    class BreachersMatch():
        def __init__(self, id, players, timestamp, game_data):
            self.id = id
            self.players = players
            self.timestamp = timestamp #UTC
            self.game_data = self.MatchData(**game_data)
        
        def __repr__(self):
            return(
                f"<BreachersMatch id={self.id}, players={self.players}, timestamp={self.timestamp}, game_data={self.game_data}>"
            )
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
            
            def __repr__(self):
                return(
                    f"<MatchData MapName={self.MapName}, matchMode={self.matchMode}, matchType={self.matchType}, players={self.players}, playersLeft={self.playersLeft}, allPlayers={self.allPlayers}>"
                )
            
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
                
                def __repr__(self):
                    return(
                        f"<MatchPlayer ApiId={self.ApiId}, clanTag={self.clanTag}, GameMatchDataResult={self.GameMatchDataResult}, score={self.score}, gameTimeInSeconds={self.gameTimeInSeconds}, "
                        f"gameTime={self.gameTime}, mvp={self.mvp}, penaltyReason={self.penaltyReason}, rounds={self.rounds}, timeAfk={self.timeAfk}, Username={self.Username}>"
                    )
                
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
                            self.gadgets.append(self.BreachersGadget(**gadget))
                        self.weapons = []
                        for weapon in weapons:
                            self.weapons.append(self.BreachersWeapon(**weapon))
                    
                    def __repr__(self):
                        return(
                            f"<MatchPlayerRound ace={self.ace}, assists={self.assists}, botAssists={self.botAssists}, deaths={self.deaths}, firstBlood={self.firstBlood}, mvp={self.mvp}, "
                            f"roundNumber={self.roundNumber}, roundTime={self.roundTime}, team={self.team}, teamWon={self.teamWon}, gadgets={self.gadgets}, weapons={self.weapons}"
                        )

    def get_user_match(self, BreachersUserId, json=False):
        '''
        `BreachersUserId` The id of a breachers user\n
        `json` if True return user as json otherwise returns `BreachersUser` object
        '''
        encoded_id = urllib.parse.quote(BreachersUserId)
        result = requests.get(f'{self.base_url}BreachersApi/get_match_data?player_id='+encoded_id)
        print(result.status_code)
        if result.ok:
            if json:
                return result.json()
            else:
                matches = []
                for i in result.json():
                    matches.append(self.BreachersMatch(**i))
                return matches
        else:
            raise ValueError(f"Request error {result.status_code}")
        



    class BreachersGadget():
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
        
        def __repr__(self):
            return (f"<BreachersGadget Name={self.Name}, botDamageDone={self.botDamageDone}, botKills={self.botKills}, damageDone={self.damageDone}, "
            f"destroyed={self.destroyed}, enemyTriggered={self.enemyTriggered}, friendlyDamageDone={self.friendlyDamageDone}, kills={self.kills}, "
            f"teamHealed={self.teamHealed}, triggered={self.triggered}, used={self.used}>"
            )
    class BreachersWeapon():
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
        
        def __repr__(self):
            return (f"<BreachersWeapon Name={self.Name}, botDamageDone={self.botDamageDone} botHeadshotKills={self.botHeadshotKills}, botKills={self.botKills}, "
                    f"damageDone={self.damageDone}, friendlyDamageDone={self.friendlyDamageDone}, headshotKills={self.headshotKills}, shotsFired={self.shotsFired}, "
                    f"totalHeadshots={self.totalHeadshots}, totalKills={self.totalKills}, totalShotsHit={self.totalShotsHit}>"
            )