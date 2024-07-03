from api import api



x = input("username:\n>>")
users = api.search_users(x)

for user in users:
    print(f"({user.id}) #{user.clanTag} {user.userName}\n")

x = input("ID:\n>>")
query = api.get_user(x)
print(f"({query.id}) #{query.clanTag} {query.userName}\n")

x = input("ID:\n>>")
query = api.get_user_match(x, 0, True)
print(query)