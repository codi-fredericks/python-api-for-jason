import api


x = input("ID:\n>>") #get breachers id from user
query = api.User.get_user(x) #search api for user
print(f"({query.id}) #{query.clanTag} {query.userName}\n") #print user