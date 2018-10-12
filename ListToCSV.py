 
import json
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

add_shelter = ("INSERT shelters ( shelter_name,shelter_address,shelter_phone_number, shelter_city, shelter_zip, shelter_email, shelter_latitude, shelter_longitude, shelter_ID) OUTPUT INSERTED.ID VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)")  
add_pet= ("INSERT  pets ( pet_name, pet_breed1, pet_breed2, pet_gender, pet_description, pet_details,  pet_lastUpdated, pet_photosLink, shelter_ID, pet_ID, pet_type) OUTPUT INSERTED.ID VALUES (?,?, ?, ?, ?, ?, ?, ?, ?,?,?)")  
petList = list()
shelterList = list()





def getPetsJson():

    with open('pets_dict.json') as file:
         petsDict = json.load(file )
    
    return(petsDict)
    
def getSheltersJson():
    
     with open('shelter_dict.json') as file:
         sheltersDict = json.load(file )
     
     return(sheltersDict)

 
 

def insertShelters(sheltersDict):
 
 
     
 
    for shelter in sheltersDict:
      #  print(shelter)
       shelterDict= dict()
       
       shelterDict["name"] =  shelter['name']['$t']
       if any(shelter['address1']):
           shelterDict["address"] =  shelter['address1']['$t']
       else:
           shelterDict["address"] = 'N/A'
       
       if any(shelter['phone']):
           shelterDict["phone"] =  shelter['phone']['$t']
       else:
           shelterDict["phone"] = 'N/A'
       shelterDict["city"] =  shelter['city']['$t']
       shelterDict["zipCode"]  =  shelter['zip']['$t']
       shelterDict["email"] =   shelter['email']['$t']
       shelterDict["lat"]  =  shelter['latitude']['$t']
       shelterDict["long"] = shelter['longitude']['$t']
       shelterDict["shelterID"] =   shelter['id']['$t']
       
       shelterList.append(shelterDict);
 
 

def insertPets(petsDict):
#Start SQL Operation
#Connect to Database 
 
 
    for pet in petsDict:
       petDict= dict()
        
       petDict["pet_name"] =  pet['name']['$t']
        
       if any(pet['media']):
               petDict["pet_photosLink"] = str( pet['media']['photos']['photo'][0]['$t'].split('&')[0])+ '&width=300&-pn.jpg' 
       else:
              petDict["pet_photosLink"] = 'N/A'
       petDict["pet_gender"] = pet['sex']['$t']
       if any(pet['description']):
              # petDict["pet_description"] = pet['description']['$t'].replace("doesnâ\x80\x99t", "doesn't") 
              petDict["pet_description"] = pet['description']['$t'].encode("latin1").decode("utf-8", "ignore")
              #print(pet_description)
#               print(" ")
       else:
               petDict["pet_description"] = 'N/A'
       #print(pet_description)
       petDict["pet_lastUpdated"] = pet['lastUpdate']['$t']
       petDict["pet_type"]= pet['animal']['$t']
       petDict["pet_ID"] =  pet['id']['$t']
       petDict["shelter_ID"] = pet['shelterId']['$t']
       #petDict["pet_breeds"] = pet['breeds']['breed']
       pet_breeds =  pet['breeds']['breed']
       if isinstance(pet_breeds, list):
          petDict["pet_breed1"]  = pet_breeds[0]['$t']
          petDict["pet_breed2"]  = pet_breeds[1]['$t']
           
       else:
           petDict["pet_breed1"]  = pet_breeds['$t']
           petDict["pet_breed2"]  = "N/A"
       
       if any(pet['options']):
           petDict["pet_detail"]   = pet['options']['option']
           
           detailHolder = ""
           for detail in  petDict["pet_detail"]:
               if isinstance(detail, dict):
                    petDict["pet_detail"] = detail['$t']
                    #detailHolder = detailHolder + " " + pet_detail
    
               else:
             #      detailHolder = detail
    #               print(pet_detail, "flaggg")
                  print("")
               
       petList.append(petDict);
 
petsDict = getPetsJson()
sheltersDict = getSheltersJson()

insertShelters(sheltersDict)
insertPets(petsDict)
 
#newList = list()
#newList.append(petList[0])
#newList.append(petList[17])

print(petList[16]['pet_photosLink']   )
 
with open('pets_test.json', 'w') as file:
      json.dump(petList, file)

with open('shelters_test.json', 'w') as file:
      json.dump(shelterList, file) 