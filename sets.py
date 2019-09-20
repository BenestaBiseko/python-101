'''
Write a simple script to demonstrate your understanding of sets as data types 
'''
'''
https://github.com/BenestaBiseko/python-101/compare/master...develop

'''

foodset = {"beans", "cocunut", "mangoes", "meat", "peanut"}
#del foodset
for x in foodset:
     print(x.upper(), end=" ") 

cityset = {"Dodoma", "Arusha", "Nairobi", "Kampala"}
cityset.update(["Beijing", "Moscow", "Lusaka"])
cityset.remove("Beijing")
for y in cityset:

    print(y.upper(), end=" ")
    print(len(y))
allset = foodset.union(cityset)
print(allset)
cityset.update(foodset)
print(cityset)

