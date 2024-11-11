import random
from fake_useragent import UserAgent

User_Agent = UserAgent()
ua1 = User_Agent.chrome

ua2 = User_Agent.random
print("ua.chrome : {ua1} \n\n ua.random : {ua2}")
