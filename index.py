users=["david","ae","eee"]
user2=["test1","test3","tes3"]
users.extend(user2)
user3=users.copy()
for user in users:
    print(user)
print(len(users))
user3.sort()