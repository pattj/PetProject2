# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:41:28 2018

@author: J
"""
 
from __future__ import print_function
import requests
from requests_oauthlib import OAuth1
import json
from bs4 import BeautifulSoup
import csv
 
import mysql.connector
from mysql.connector import errorcode 

randomPetUrl = 'http://api.petfinder.com/pet.getRandom'
findShelterUrl = 'http://api.petfinder.com/shelter.find'
getPetsUrl = 'http://api.petfinder.com/shelter.getPets'

api_token = "48798206822b11ada6e1ad4c3cfdfa67"
auth = OAuth1(api_token)
 
TABLES = {}
TABLES['shelters'] = (
    "CREATE TABLE `shelters` ("
    "  `shelter_name` varchar(20) NOT NULL ,"
    "  `shelter_address` varchar(20) NOT NULL ,"
    "  `shelter_phone_number` varchar(20) NOT NULL ,"
    "  `shelter_city` varchar(20) NOT NULL ,"
    "  `shelter_zip` varchar(20) NOT NULL ,"
    "  `shelter_email` varchar(20) NOT NULL ,"
    "  `shelter_coords` float(8,4) NOT NULL AUTO_INCREMENT,"
    "  PRIMARY KEY (`shelter_coords`)"
    ") ENGINE=InnoDB")

TABLES['pets'] = (
    "CREATE TABLE `pets` ("
    "  `pet_name` varchar(20) NOT NULL ,"
    "  `pet_breed` varchar(20) NOT NULL ,"
    "  `pet_shelter` varchar(20) NOT NULL ,"
    "  `pet_houseTrained` varchar(20) NOT NULL ,"
    "  `pet_description` varchar(20) NOT NULL ,"
    "  `pet_lastUpdated` varchar(20) NOT NULL ,"
    "  `pet_photosLink` float(8,4) NOT NULL AUTO_INCREMENT,"
    "  PRIMARY KEY (`shelter_coords`)"
    ") ENGINE=InnoDB")

add_shelter = ("INSERT INTO shelter "
               "(shelter_name,shelter_address,shelter_phone_number, shelter_city, shelter_zip, shelter_email, shelter_coords)"
               "VALUES (%(shelter_name)s, %(shelter_address)s, %(shelter_phone_number)s, %(shelter_city)s, %(shelter_zip)s, %(shelter_email)s, %(shelter_coords)s)"
               )



#Start SQL Operation
#Connect to Database 
#cnx = mysql.connector.connect(user='sql3239242', password='hfvchGcufw',
#                                 host='sql3.freesqldatabase.com',
#                                 database='sql3239242')
#
#cursor = cnx.cursor()

#for name, ddl in TABLES.items():
#    try:
#        print("Creating table {}: ".format(name), end='')
#        cursor.execute(ddl)
#    except mysql.connector.Error as err:
#        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#            print("already exists.")
#        else:
#            print(err.msg)
#    else:
#        print("OK")
#
#cursor.close()
#cnx.close()


randomPetHeaders = {
        
        'Key' : api_token,
        'Animal' : 'dog',
         'output': 'basic',
         'format':'json'
         
        
        }


sheltersHeaders = {
        
        'key': api_token,
        'location' :"Nevada",
        'format': 'json'
        
        }


class Shelter:
     shelter_name = ""
     shelter_address = ""
     shelter_phone_number = "" 
     shelter_city = " "
     shelter_zip  = 0
     shelter_email = " "
     shelter_latitude = 0.0
     shelter_longitude = 0.0
       
     def __init__(self,shelter):
         self.shelter_address = shelter
         
         
 

def getRandomPet( ):
    response = requests.get(randomPetUrl,randomPetHeaders) 
    soup = BeautifulSoup(response.text, "html.parser")
    newDictionary = json.loads(str(soup.text))
    for key, value in newDictionary['petfinder'].items():
        print(key)
    print(newDictionary['petfinder']['pet']['name']  )


#Return a list of shelter dictionary
def getSheltersInNV():    
    response = requests.get(findShelterUrl,sheltersHeaders) 
    soup = BeautifulSoup(response.text, "lxml")
    newDictionary = json.loads(str(soup.text))
    #for key, value in newDictionary['petfinder']['shelters'].items():
    #    print(key)
    # 
    sheltersInNV = newDictionary['petfinder']['shelters']['shelter']
    shelterList = []
    for shelter in sheltersInNV:
         shelterList.append(shelter)
    return shelterList

 
def getPetsFromShelters(shelterList):
    petsList = []
    for shelter in shelterList:
         shelterHeaders = {
                
                'key': api_token,
                'id':  shelter['id']['$t'],
                'format': 'json'
                
                }
            
         response = requests.get(getPetsUrl,shelterHeaders) 
         soup = BeautifulSoup(response.text, "lxml")
         newDictionary = json.loads(str(soup.text))
         pets = newDictionary['petfinder']['pets']
         
         if ( any(pets)):
             #print (shelter['id'])
             pets2 = newDictionary['petfinder']['pets']['pet']
              
             for pet in pets2:
                #If the pet object is a dict, append it, else append there's only one pet, append 'pets2'
                if isinstance(pet,dict):
                    petsList.append(pet)
                else:
                    petsList.append(pets2)
                    break 
                 
#         print ("----------------------------------------- ")
        
    return petsList

 



#def parseSheltersToDB(shelterList):
    
    



response = requests.get(randomPetUrl,randomPetHeaders) ;


#shelterList = getSheltersInNV()
#with open('shelter_dict.json', 'w') as file:
#        json.dump(shelterList, file)
#        file.write('\n')
 
 
#petList = getPetsFromShelters(shelterList)
#with open('pets_dict.json', 'w') as file:
#      json.dump(petList, file)

#index = 0;
#for pet in petList:
#    print (pet.keys())
#    index = index +1
 