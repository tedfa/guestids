import pickle

netids = pickle.load(open('logwrite.p', 'rb+'))
print(netids)

# To change a single or more password value in the dictionary
# Uncomment following code and adjust key and password values

# for item in netids:
#     netids[1] = 'Pineapple7'
#
#
# pickle.dump(netids, open('logwrite.p', 'rb+'))