import api
import json


#JSON Output
id = input("ID:\n>>")
query = api.Matches.get_user_match(BreachersUserId=id, json=True)
match_num = int(input("Match Number\n>>"))
print(query[match_num])


#Object Output
id = input("ID:\n>>")
query = api.Matches.get_user_match(BreachersUserId=id, json=False)
match_num = int(input("Match Number\n>>"))
match = query[match_num]

for player in match.game_data.players:
    if player.ApiId == id:
        print(f"Score: {player.score}\nMVP: {player.mvp}\n")
        for round in player.rounds:
            print(f"Round: {round.roundNumber}\nSide: {round.team}\nMVP: {round.mvp}\nAce: {round.ace}\nDeaths: {round.deaths}")
            print("-"*25)
