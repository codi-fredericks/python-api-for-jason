import api

x = input("username:\n>>") #get input from user
users = api.User.search_users(x) #search api for user

for user in users: #iterate through users
    print(f"({user.id}) #{user.clanTag} {user.userName}\n") #print user