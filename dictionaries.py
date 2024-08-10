#Dictionary using inbuilt
mydict =dict()
print(mydict)
#using key and value pair
mydict =dict( JAYA= "parinith" , amama="Shreya")
print(mydict)
#not using Dictionary values
mydict = {"AMMA":"appa", "Shreya":"parinith"} 
print(mydict)
#traversing through the dictionary values
def traverse(mydict):
  for key in mydict:
    print(key,mydict[key])
traverse(mydict)
#searching the for the element in the history
def search(mydict,value):
  for key in mydict:
    if mydict[key] == value:
      return key,value
search(mydict,'parinith')    

#deleting the parameter
del mydict['AMMA'] 
print(mydict)
#using function using parenthesis
#using operations use[]

#pop is used for deleting element
#popitem is used for deleting the last element
#mydict.pop()
#mydict.popitem()

print(mydict.copy())

#using fromkeys methods will be creating new dictionary

newdict ={}.fromkeys([1,2,3],0)
print(newdict)

#prints all the key value pair in the items

print(newdict.items())

print(newdict.keys())

print(newdict.values())

#using in or bot opeartors

updict = {1:"one",2:"two",3:"three"}
print("three" in updict.values())

