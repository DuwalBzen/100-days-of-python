import random

friends = [
    "Alex",
    "Bob",
    "Charlie",
    "David", ]

# # 1st Option
# print(random.choice(friends))
#
# # Second Option
# random_index = random.randint(0, len(friends) + 1)
# print(friends[random_index])


# Index Error
length = len(friends)
print(friends[length - 1])
