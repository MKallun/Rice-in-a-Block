# IMPORTANT NOTICE
Due to rappler, our source of news for the new tab, updating their website today (07/14/2020 8:00am) we sadly are experiencing technical issues on our new tab,
we are working on a substitute but we are sadly not sure if we will be able to find a news source that will fit all criteria we require

thank you for understanding
# Update
Changed news source from rappler to agriculture.einnews, some issues might persist due to website constraints
# =============================================


# Rice-in-a-Block

watch the trailer https://youtu.be/3S-k2hOhlcQ


# SET-UP
please install python 3.8 and add it to PATH
  for more info : https://www.youtube.com/watch?v=bnhQBUEpWlg (video not owned by us)

open cmd, install libraries/frameworks using this command, enter each line 1 by 1 (e.g pip install -U pip, wait for it to finish downloading and installing before installing the next line), please install all of them.

* pip install -U pip
* pip install dash
* pip install dash-renderer
* pip install dash-html-components
* pip install dash-core-components
* pip install dash-bootstrap-components
* pip install plotly
* pip install plotly_express
* pip install web3
* pip install pandas
* pip install dash-enterprise-auth
* pip install dash-auth
* pip install bs4
* pip install flask
* pip install request

# RUNNING THE PROGRAM

Aside from compiling and running RBModified.sol in remix.ethereum.org you'll need to open admin.py, consumer.py and stresstest.py in VS Code, then replace these following lines in each file to the web3 address provided by remix when you run the smart contract 
line 15 in stresstest.py
line 56 in admin.py
line 47 in consumer.py


# ENTERING DATA 

There are 2 ways of entering Data
1. Random Data Entry
  - this method involves running the stresstest.py, after changing line 15 to the address provided by remix.ethereum.org and running it, you will be asked to enter the amount of random data you want, in VS Code Terminal, say you entered 5 then 5 random data will be added to the chain. this method is advisable if you want to open the app and see the graphs and table already populated and/or if you find manually inserting data 1 by 1 tedious
(before entering please keep in mind that since this will run locally you might want to consider how powerful you desktop/laptop is since it will bear the full burden of reading and writing everything)

2. Single Data Entry 
  - this method involves entering data from admin.py, after changing line 56 to the address provided by remix.ethereum.org and running it, you can open chrome the go to http://127.0.0.1:8050/ now depending on your laptop/desktops speed you might need to wait for a while before you can go to this address a good way to check if its already good to go is checking VS Codes terminal and waiting till you see this

Running on http://127.0.0.1:8050/
Debugger PIN: 779-178-752
 * Serving Flask app "INSERT_APP_NAME_HERE" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
Running on http://127.0.0.1:8050/
Debugger PIN: 869-638-768

after going to webpage you will be aske to login, two accts are prepared
acct 1
Username : admin
Password : 1234

acct2
Username : test
Password : test

after logging in you can see on the left side of the webpage the field for data entry 
Manufacturer = accepts name of the rice manufacturer
Brand = accepts name of the rice brand (e.g dinurado)
Area = drop down, accepts REGION I to BARMM
Weight = accepts rice weight in KG (e.g. 320 for 320 kg)
Price = accepts price set by manufacturer per KG (e.g. 32 for 32php/kg)
Status = drop down, select between Delivered and Recived, if you sent your rice to another area, its Delivered, if you recieved it from another area its Recieved
Status Recieved = drop down, select between complete, damaged and stolen, enabled when Status chosen is Recieved
Status weight = accepts weight of rice damaged or stolen, value is 0 if status recieved is complete

after entering all info, press submit, wait for confirmation then wait for webpage to update

# VIEWING DATA

There are 2 ways to view data the first one is through admin.py and the second one is through consumer.py the only difference is that consumer.py doesnt allow user input and is generally for public consumption

There area 4 tabs in both admin.py and consumer.py 
1. Area graph = bargraph showing total rice each region currently have in kg
2. Date graph = bargraph showing total rice all region have in kg per month 
3. List = table showing all transactions, in admin.py list has another column showing who encoded the data
4. News = shows a list of rice related news, if you click on the headline you will be redirected to the website containing the news



# things we planned to add but sadly wasn't able to:
1. add a way to view the full detail of the transaction if you click who encoded the entry in admin.py
2. add a line graph in date graph to show the expected rice supply at that month 
3. update the login, from basic auth to plotly oauth, we cant since its a paid service 


