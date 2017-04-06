import pickle


def load_dict_data(array, newpass):
    netids = pickle.load(open('logwrite.p', 'rb+'))
    # function goes here that starts the selenium scripts
    for elms in array:
        netids[elms] = newpass
    pickle.dump(netids, open('logwrite.p', 'rb+'))


space = "&nbsp;" * 30
small_space = "&nbsp;" * 15
items = []

while 1:
    item = int(input("Enter the number of the ID to reset "))
    if item == -1:
        break
    items.append(item)
    # if len(items) == 4:
    #     break
    print(item)
print("\n")
print(items)

newpwd = input("Enter new password ")
print("\n")

# Data structure function goes here.
# Function will use the values of the items list to make the appropriate key value changes
# to the netids disctionary. That will then be saved to a file via pickle
load_dict_data(items, newpwd)

starter_template = "Guest Log-in {} | {} |  Guest Log-in {} |\n---- | ---- |  ---- |\n".format(space, small_space, space)
my_file = open('login.md', 'w')
# my_file.write(starter_template)
flag = True
count = 0
for elems in items:
    my_file.write('**Guest Log-in** {} | {} | **Guest Log-in** {} \n'.format(space, small_space, space))
    if flag:
        my_file.write('| ---- | ---- | ---- |\n')
        flag = False
    my_file.write('**Give this log-in to Patron**  |  |  **Keep this log-in** |\n')
    my_file.write('Username: Lib{} | | Username: Lib{} |\n'.format(elems, elems))
    my_file.write('Password: {0} | | Password: {1} |\n'.format(newpwd, newpwd))
    my_file.write('Log-in is valid for 24 hours | | Log-in is valid for 24 hours |\n')
    my_file.write('    | |   \n')
    count += 1
    if count == 4:
        my_file.write('<div style="page-break-after: always;"></div>\n')
        my_file.write('\n')
        flag = True
        count = 0
my_file.close()
