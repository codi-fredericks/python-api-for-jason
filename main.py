from api import api
import json


x = input("username:\n>>")
users = api.search_users(x)

for user in users:
    print(f"({user.id}) #{user.clanTag} {user.userName}\n")
'''
x = input("ID:\n>>")
query = api.get_user(x)
print(f"({query.id}) #{query.clanTag} {query.userName}\n")
'''

'''
#JSON Output
x = input("ID:\n>>")
query = api.get_user_match(x, True)
match_num = int(input("Match Number\n>>"))
with open(f'data/{(api.get_user(x).userName)}_data.json', 'w', encoding='utf-8') as f:
    json.dump(query[match_num], f, ensure_ascii=False, indent=4)
'''

#Object Output
x = input("ID:\n>>")
query = api.get_user_match(x, False)
match_num = int(input("Match Number\n>>"))
match = query[match_num]

for player in match.game_data.players:
    if player.ApiId == x:
        print(f"Score: {player.score}\nMVP: {player.mvp}\n")
        for round in player.rounds:
            print(f"Round: {round.roundNumber}\nSide: {round.team}\nMVP: {round.mvp}\nAce: {round.ace}\nDeaths: {round.deaths}")
            print("-"*25)