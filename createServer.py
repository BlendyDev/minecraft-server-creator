import requests
import platform
import download
import json
from os.path import exists

versions = ["1.19", "1.18.2", "1.17.1", "1.16.5", "1.15.2", "1.14.4", "1.13.2", "1.12.2", "1.11.2", "1.10.2", "1.9.4", "1.8.8"]
files = ["vanilla", "paper","fabric", "forge"]
softwares = ["Vanilla", "Paper", "Fabric", "Forge"]

def setup():
    #Startup script + EULA
    RAM = input("Enter Amount of ram in GB: ")
    RAM = int(RAM)
    if platform.system() == "Windows":
        sb = open("../start.bat", "w")
    else:
        sb = open("../start.sh", "w")
        sb.write("#!/bin/sh\n")
    sb.write(f"java -Xmx{RAM}G -jar Server.jar")
    sb.close()
    eula = open("../eula.txt", "w")
    eula.write("eula=true")
    eula.close()
    
def downloadSoftware(index):
    #Software chooser
    f = open("json/" + files[index] + ".json")
    data = json.load(f)
    print("")
    print("*"*20)
    print(softwares[index] + " versions:\n")
    i = 1
    for version in data["Versions"]:
        print(f"{i} # {version}")
        i = i+1
    print("*"*20)
    verid = int(input("Enter id: "))
    
    while (not (verid > 0 and verid <= len(data["Versions"]))):
        print("Invalid Option")
        verid = int(input("Enter id: "))
    v = data[versions[verid-1]]
    setup()
    download.download(v, "../Server.jar")
    f.close()   
    print("Server successfully setup!")
    
def menu():
    #Start UI
    print("*"*20)
    i = 1
    for sw in softwares:
        print(f"{i} # {sw}")
        i = i+1
    print("*"*20)
    chosenSw = int(input("Please entesr id: "))
    while (not (chosenSw > 0 and chosenSw <= len(softwares))): 
        print("Invalid Option")
        chosenSw = int(input("Please enter id: "))
    downloadSoftware(chosenSw-1)
    
if (not exists("eula.txt")):
    input("This program will auto-agree to the Minecraft EULA (https://aka.ms/MinecraftEULA). If you don't agree with it please halt this program.\n[PRESS ENTER TO CONTINUE AND IGNORE THIS WARNING FOR FUTURE USES]\n")
    ignoreWarning = open("eula.txt", "w")
    ignoreWarning.close()
            
menu()
