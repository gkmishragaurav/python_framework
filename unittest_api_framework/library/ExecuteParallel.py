import requests

def get_user(user_name):
  try:
    final_url = 'https://petstore.swagger.io/v2/user/{}'.format(user_name)
    header = {'Accept': 'application/json'}
    response = requests.get(final_url, headers=header)
    print response
    return response
  except Exception as e:
    print(e)
    return False

from multiprocessing import Pool
DEFAULT_POOL_SIZE=1

# # with pool - get user
p = Pool(1)
res = p.map(get_user, [ 'string'])
print res
p.close()


# import time
# # with pool create user
# user1 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user2 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user3 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user4 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user5 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user6 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user7 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user8 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
#
# users = [user1,user2,user3,user4,user5,user6,user7,user8]
# t1=time.time()
# res = p.map(create_user, users)
# t2=time.time()
# print res, t2-t1

#1- 8.6323890686
#2- 4.40179204941
#3- 3.73401808739
#4- 2.30057096481
#5- 2.28681302071
#8- 1.35835194588

# # with pool update user
# user1 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user2 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user3 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user4 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user5 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user6 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user7 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# user8 = ['abc', 'abc', 'abc', 'abc', 'abc', '123']
# users = [user1,user2,user3,user4,user5,user6,user7,user8]
# res = p.map(update_user, users)
# print res





# work_load = [get_user, create_user]
# args = [(), ('abc', 'abc', 'abc', 'abc', 'abc')]
# work_load = [ create_user]
# args = ('abc', 'abc', 'abc', 'abc', 'abc')


# print ececute_parallel(work_load, args)
# print create_user('abc', 'abc', 'abc', 'abc', 'abc')