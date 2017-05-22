# This script initializes the dictionary data structure that the passwords are stored in.
# Only run once.
# It will create the dictionary and then write that information to a file called logwrite.p
# logwrite.p is then opened in gid4.py and manipulated.
import pickle



netids = {1: 'Fresh123', 2: 'Fresh123', 3: 'Fresh123', 4: 'Fresh123', 5: 'Fresh123', 6: 'Fresh123', 7: 'Fresh123',
          8: 'Fresh123', 9: 'Fresh123', 10: 'Fresh123', 11: 'Fresh123', 12: 'Fresh123', 13: 'Fresh123', 14: 'Fresh123',
          15: 'Fresh123', 16: 'Fresh123', 17: 'Fresh123', 18: 'Fresh123', 19: 'Fresh123', 20: 'Fresh123'}

print(netids)

#netids[3] = 'Orange27'
#print('\n')
print(netids)

pickle.dump(netids, open('logwrite.p', 'wb'))

# print(lib1['netid'])
# print(lib1['password'])
# print('\n')
# lib1['password'] = 'Orange27'
# print(lib1['netid'])
# print(lib1['password'])



  #  pickle.dump(lib, open('logwrite.p', 'wb'))
