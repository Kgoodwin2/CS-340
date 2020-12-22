From pymongo import MongoClient
From bson.Objectid import Object Id

Class Animals (object):
def_init_(self,user,password):
#initialize MongoClient
self.client=
MongoClient(‘mongodb://%s:%@localhost:51840’%(user,password)
self.database = Self.Client[‘AAC’]
#This is for the create in CRUD
def create(self, animal_info):
if animal_info is not None:
print(“Inserting Information”)
self.database.AAC.insert_one(animal_info)
#if successful insert
Print(“True”)
else:
raise Exception (“False”)
#Here is the R in CRUD
#line below is used to find an animal by name
#I used age since it is bound to return multiple results
If criteria is not None:
#finds data by age
data = self.database.AAC.find(age)
for document in data:
print (“True”)
print (document)
else:
raise Exception (“False”)
#Here is the U for Update in CRUD
self.database.animal_info.delete(name)
else:
raise Exception (“error no data found”)
#Update a name
def update (self, name, newName):
if name is not None and newname is not None:
#Update set new name
self.database.AAC.update(name, {‘$ set’: newname})
else:
raise Exception (“no data to update”)
#Here is the delete in CRUD
#deletes an animal name not a breed but a name since it will return more narrow results 
def delete (self, name)
if age is not None :
data = Self.read(name)
if data is None:
print (“Error”)
return
