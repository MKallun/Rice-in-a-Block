import json
import xlwt # to write excel spread sheet
import datetime
from datetime import date # to get date today
from random import randint # for random integer value
from xlwt import Workbook # create workboox
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[{"internalType":"string","name":"_UserName","type":"string"}],"name":"Login","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_UserName","type":"string"},{"internalType":"string","name":"_Password","type":"string"}],"name":"Register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_User","type":"string"},{"internalType":"string","name":"_Manufacturer","type":"string"},{"internalType":"string","name":"_Brand","type":"string"},{"internalType":"string","name":"_Area","type":"string"},{"internalType":"string","name":"_Status","type":"string"},{"internalType":"string","name":"_StatusRecieved","type":"string"},{"internalType":"uint256","name":"_StatusWeight","type":"uint256"},{"internalType":"uint256","name":"_Date","type":"uint256"},{"internalType":"uint256","name":"_Year","type":"uint256"},{"internalType":"uint256","name":"_Month","type":"uint256"},{"internalType":"uint256","name":"_Day","type":"uint256"},{"internalType":"uint256","name":"_Weight","type":"uint256"},{"internalType":"uint256","name":"_Price","type":"uint256"}],"name":"enterRiceInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getArea","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getBrand","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getManu","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getMonth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatus","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusRecieved","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTransID","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getUser","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getYear","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"newcount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"transactionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

#needs to be changed to match address in remix solidity
address = web3.toChecksumAddress("0xF5Aeb9F211522A8eeAD06A1c105DeceCbB8339a2")

contract = web3.eth.contract(address=address, abi=abi)

#loops function
alpha = input ("How many times do you want to run the test? : ")
print("running test for", alpha, "times")
cstatW = 0
for i in range(0, int(alpha)): #loop 10,000 times for stress test
    x = randint(500, 1000) #random value for weight
    y = randint(50, 70) #random value for price 
    z = randint(1, 16) #random value for area, manufacturer, brand
    a = randint(1, 3)
    b = randint(1, 3)
    c = randint(1, 2)
    d = randint(1, 3)
    e = randint(1, 499)
    username = 'testprogram'
    dates = datetime.date.today()

    if (z == 1):
        zarea = 'REGION I'
    elif (z == 2):
        zarea = 'REGION II'
    elif (z == 3):
        zarea = 'REGION III'
    elif (z == 4):
        zarea = 'REGION IV'
    elif (z == 5):
        zarea = 'REGION V'
    elif (z == 6):
        zarea = 'REGION VI'
    elif (z == 7):
        zarea = 'REGION VII'
    elif (z == 8):
        zarea = 'REGION VIII'
    elif (z == 9):
        zarea = 'REGION IX'
    elif (z == 10):
        zarea = 'REGION X'
    elif (z == 11):
        zarea = 'REGION XI'
    elif (z == 12):
        zarea = 'REGION XII'
    elif (z == 13):
        zarea = 'REGION XIII'
    elif (z == 14):
        zarea = 'NCR'
    elif (z == 15):
        zarea = 'BARMM'
    elif (z == 16):
        zarea = 'CARAGA'
    
    if (a == 1):
        zman = 'concorp'
    elif (a == 2):
        zman = 'sahara'
    elif (a == 3):
        zman = 'idea corp'
    
    if (b == 1):
        zbra = 'riceplus'
    elif (b == 2):
        zbra = 'riceplusplus'
    elif (b == 3):
        zbra = 'ricesurplus'

    if (c == 1):
        cstat = 'Recieved'
    elif (c == 2):
        cstat = 'Delivered'

    if (c == 1):
        
        if (d == 1):
            cstatR = 'Complete'
            cstatW = 0
        elif (d == 2):
            cstatR = 'Stolen'
            cstatW = e
        elif (d == 3):
            cstatR = 'Damaged'
            cstatW = e
    else:
        cstatR = 'Complete'


    remW = int(x)-int(e)

    datey = str(dates.year)
    datem = str(dates.month)
    dated = str(dates.day)
    
    Date = datey+datem+dated 
    Manufacturer = zman
    Brand = zbra
    Area = zarea
    Weight = x
    Status = cstat
    StatusRecieved = cstatR
    StatusWeight = cstatW
    RemainingWeight = remW
    Price = y
    tx_hash = contract.functions.enterRiceInfo(str(username), str(Manufacturer), str(Brand), str(Area), str(Status), str(StatusRecieved), int(StatusWeight), int(Date), int(datey), int(datem), int(dated), int(Weight), int(Price)).transact()
    trans = web3.toHex(tx_hash)
    print("The Transaction hash is : ",trans)
    print("Data Added : ",i+1)
    print("")

print("random data entered, added",alpha,"in total")


#to display all info
#comment all to temporarily disable
# ------------------------------------------- 
#retID = input("Enter Entry ID to be retrived : ")
#print(contract.functions.GetRiceInfo(int(retID)).call())
#
# ------------------------------------------- 