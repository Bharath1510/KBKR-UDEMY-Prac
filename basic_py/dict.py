dict = {'a':'apple','b':'ball','c':'cat'}
print(dict['b'])
dict['b']='bat'
print(dict['b'])
list_dict = [{1:'one',2:'two',3:'three'},{1:'a',2:'b'}]
print(list_dict)
print(list_dict[1])
print(list_dict[0][3])
bag = {
    'books':{'name':'science','pages':'100'},
    'stationery':[{'name':'pencil','quantity':'1'},{'name':'pen','quantity':'2'}],
    'colour':'black'
}
print(bag)
print(bag['stationery'])
print(bag['stationery'][1])
print(bag['stationery'][1]['name'])

