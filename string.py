'''
Write a simple script to demonstrate your understanding of strings 
'''
Habari = """This is the beginning of python {} coures
it demonstrates different thing and some of concepts in python
I would like to inform you to collaborate with us in this course {}"""
version = 101
year = 2019
print(Habari.upper())
print(Habari[132:152].upper())
print(Habari.replace("T", "Hello t"))
print(len(Habari))
part = "inform you to collaborate with us" in Habari
print(part)
print(Habari.format(version, year).upper())
