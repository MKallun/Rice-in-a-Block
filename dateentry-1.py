import json
import datetime
from datetime import date # to get date today
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]


abi = json.loads('[{"inputs":[{"internalType":"string","name":"_UserName","type":"string"}],"name":"Login","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_UserName","type":"string"},{"internalType":"string","name":"_Password","type":"string"}],"name":"Register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_Manufacturer","type":"string"},{"internalType":"string","name":"_Brand","type":"string"},{"internalType":"string","name":"_Area","type":"string"},{"internalType":"string","name":"_Status","type":"string"},{"internalType":"string","name":"_StatusRecieved","type":"string"},{"internalType":"uint256","name":"_StatusWeight","type":"uint256"},{"internalType":"uint256","name":"_Date","type":"uint256"},{"internalType":"uint256","name":"_Year","type":"uint256"},{"internalType":"uint256","name":"_Month","type":"uint256"},{"internalType":"uint256","name":"_Day","type":"uint256"},{"internalType":"uint256","name":"_Weight","type":"uint256"},{"internalType":"uint256","name":"_Price","type":"uint256"}],"name":"enterRiceInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getArea","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getBrand","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getManu","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getMonth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatus","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusRecieved","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTransID","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getYear","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"newcount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"transactionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

#needs to be changed to match address in remix solidity
address = web3.toChecksumAddress("0x921db743c34cA00d6d8dcB0A1f08f23e0b204E51")

contract = web3.eth.contract(address=address, abi=abi)

#input information

#Date = date.today(), already imported datetime tho smartcontract doesnt accept
#date formats, need to find a loophole
#Date = input ("Enter Date : ") enable this for manual date entry for testing purposes
dates = datetime.date.today()
f"{dates.month:02d}" #format to keep the month double digit e.g. 01 for january
f"{dates.day:02d}" #format to keep the day double digit e.g. 01

datey = str(dates.year)
datem = str(dates.month)
dated = str(dates.day)

Date = datey+datem+dated
print(Date)
#Will be entered using a dropdown menu in the website or app
Manufacturer = input("Enter Manufacturer : ")

#Will be entered using a dropdown menu in the website or app
Brand = input("Enter Brand : ")

#Will be entered using a dropdown menu in the website or app
Area = input("Enter Area : ")

Weight = input("Enter Weight in Kilos : ")

Price = input("Enter Price per kilo : ")

#Will be entered using a dropdown menu in the website or app (Options are Recieved and Delivered)
Status = input("Enter Status (Recieved/Delivered) : ")

#Will be entered using a dropdown menu in the website or app (Options are Damaged, Stolen and Complete)
if (Status == 'Delivered'):
    StatusRecieved = 'Complete'
elif (Status == 'Recieved'):
    StatusRecieved = input("Enter Status Recieved (Damaged/Stolen/Complete) : ")


if (StatusRecieved == 'Damaged'):
    StatusWeight = input("Enter weight of rice damaged / Lost : ")
elif (StatusRecieved == 'Stolen'):
    StatusWeight = input("Enter weight of rice Stolen : ") 
elif (StatusRecieved == 'Complete'):
    StatusWeight = 0  



tx_hash = contract.functions.enterRiceInfo(str(Manufacturer), str(Brand), str(Area), str(Status), str(StatusRecieved), int(StatusWeight), int(Date), int(datey), int(datem), int(dated), int(Weight), int(Price)).transact()

print("Date Today : ", Date)
print("The Transaction hash is : ",web3.toHex(tx_hash))