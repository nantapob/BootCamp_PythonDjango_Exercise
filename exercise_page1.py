# String Indexing
print('\r\n')
print("-- String Indexing --")
my_string = 'django'
# Goal d
print (my_string[0])
# Goal o
print (my_string[5])
# Goal djan
print (my_string[:4])
# Goal jan
print (my_string[1:4])
# Goal go
print (my_string[4:])
# Goal ognajd
print (my_string[::-1])


# Nasted Lists
# Goal Reassign "change_me" to be "changed"
print('\r\n')
print("-- Nasted Lists --")
my_list = [3,'hello',[1,4,'change_me']]
sub_my_list = my_list[2] 
sub_my_list[2] = 'changed'
# print(sub_my_list[2])
print(my_list)


# Dictionaries
# Goal  print 'print_me' from the dictionary
print('\r\n')
print("-- Dictionaries --")
d1 = {'k1':'print_me'}
d2 = {'k1':{'k2':'print_me'}}
d3 = {'k1':[{'nested_key':['37',['print_me']]}]}

print (d1['k1'])
print (d2['k1']['k2'])
print (d3['k1'][0]['nested_key'][1][0])


# Tuples
# Goal Add 5,6 and 7 to the Tuple
print('\r\n')
print("-- Tuples --")
my_tuple = (1,2,3)
my_tuple_list = list(my_tuple)
my_tuple_list.append (5)
my_tuple_list.append (6)
my_tuple_list.append (7)
my_tuple=tuple(my_tuple_list)
print(my_tuple)


# Print Formatting
# Goal Print 'Welcome to the DjanoPy BootCamp John Doe'
print('\r\n')
print("-- Print Formatting --")
first_name = 'John'; last_name = 'Doe'
print ("Welcome to the DjanoPy BootCamp", first_name ,last_name)
