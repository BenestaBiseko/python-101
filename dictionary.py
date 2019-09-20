'''
Write a simple script to demonstrate your understanding of dictionaries as data types 
'''
# here are values assigned and are printed out as dictionary datatypes  in python;
dict = {}
dict['anna'] = "Anna is {} years old"
year = 21
tinydict = {'Mockson':2012, 'Brian':2007, 'Evan':2013}
#OUTPUT

print (dict['anna'].format(year))
tinydict["Rehema"] = 2001
#del tinydict['Mockson']
print (tinydict.values())
print (tinydict.keys())
print(tinydict)
for x, y in tinydict.items():
   
    print(x,y)

if "Brian" in tinydict:

    print("Yes, 'Brian' exist in tinydic Dictionary")