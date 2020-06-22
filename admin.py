# Import Stuff here
#========================================================
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
import datetime
import dash_auth
from random import randint # for random integer value
from dash.dependencies import Input, Output, State
from datetime import date, timedelta # to get date today
from web3 import Web3
from dash.exceptions import PreventUpdate
#========================================================

VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': '1234'
}
# Stylish stuff here
#========================================================
app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO], suppress_callback_exceptions=True)

CONTENT_STYLE = {
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


# Blockchain stuff here
#========================================================

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]


abi = json.loads('[{"inputs":[{"internalType":"string","name":"_UserName","type":"string"}],"name":"Login","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_UserName","type":"string"},{"internalType":"string","name":"_Password","type":"string"}],"name":"Register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_Manufacturer","type":"string"},{"internalType":"string","name":"_Brand","type":"string"},{"internalType":"string","name":"_Area","type":"string"},{"internalType":"string","name":"_Status","type":"string"},{"internalType":"string","name":"_StatusRecieved","type":"string"},{"internalType":"uint256","name":"_StatusWeight","type":"uint256"},{"internalType":"uint256","name":"_Date","type":"uint256"},{"internalType":"uint256","name":"_Year","type":"uint256"},{"internalType":"uint256","name":"_Month","type":"uint256"},{"internalType":"uint256","name":"_Day","type":"uint256"},{"internalType":"uint256","name":"_Weight","type":"uint256"},{"internalType":"uint256","name":"_Price","type":"uint256"}],"name":"enterRiceInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getArea","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getBrand","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getManu","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getMonth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatus","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusRecieved","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTransID","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getYear","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"newcount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"transactionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

# needs to be changed to match address in remix solidity
address = web3.toChecksumAddress("0x8f73c098c4229301D3B597E32a66ff16d5F44a54")

contract = web3.eth.contract(address=address, abi=abi)

# this is the dataframwe

# Table Stuff
#========================================================

#==============================================================================

#========================================================
#Date Graph
#End of Date Graph
#========================================================

# Webpage stuff
#========================================================
# Navbar
#========================================================
navbar = dbc.NavbarSimple(
    children = [
        dbc.NavItem(dbc.NavLink("AREA GRAPH", href="/page-1", id="page-1-link")),
        dbc.NavItem(dbc.NavLink("DATE GRPAH", href="/page-3", id="page-3-link")),
	    dbc.NavItem(dbc.NavLink("LIST", href="/page-2", id="page-2-link")),
    ],
    brand="RICE-IN-A-BLOCK",
    brand_href="#",
    color="primary",
    dark=True,
)
#========================================================
# Graph
#========================================================

Graph1 = html.Div(
    [
        html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div(dcc.Graph(id='live-update-date'))),
                ]
            ),
        ]
        )
]
)

Graph2 = html.Div(
    [
        html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div(dcc.Graph(id='live-update-area'))),
                ]
            ),
        ]
        )
]
)
#========================================================
# Table
#========================================================
Table1 = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(" "))),
        dbc.Row(
            [
                #dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(dcc.Graph(id='live-update-table'))),
                #dbc.Col(html.Div(" "), width=1),
            ]
        ),
    ]
)
#========================================================
# Date Fig
#========================================================

#===============================================================
manufacturerinput = dbc.FormGroup(
    [
        dbc.Label("Manufacturer"),
        dbc.Input(type="text",id="imanufacturer"),
    ]
)
brandinput = dbc.FormGroup(
    [
        dbc.Label("Brand"),
        dbc.Input(type="text",id="ibrand"),
    ]
)
areainput = dbc.Select(
    id="iarea",
    options=[
        {"label": "old hermitland", "value": "old hermitland"},
        {"label": "new hermitland", "value": "new hermitland"},
        {"label": "shopping district", "value": "shopping district"},
    ]
)
Weightinput = dbc.FormGroup(
    [
        dbc.Label("Weight"),
        dbc.Input(id="iweight",placeholder="Kg",type="number"),
    ]
)
Priceinput = dbc.FormGroup(
    [
        dbc.Label("Price"),
        dbc.Input(id="iprice",placeholder="php/Kg",type="number"),
    ]
)
statusinput = dbc.Select(
    id="istatus",
    options=[
        {"label": "", "value": "None"},
        {"label": "Recieved", "value": "Recieved"},
        {"label": "Delivered", "value": "Delivered"},
    ],
    value = "None",
)

statusrecievedinput = dbc.FormGroup ([ #status recieved input
    dbc.Label("Status Recieved: "),
    dbc.Select(
            id="irstatus",
            options=[
                {"label": "", "value": "None"},
                {"label": "Damaged", "value": "Damaged"},
                {"label": "Complete", "value": "Complete"},
                {"label": "Stolen", "value": "Stolen"},
            ], 
            value = "Complete",
            disabled = True,
    ),
])
                    

statusweightinput = dbc.FormGroup( #status recieved weight input
    [
        dbc.Label("Status Weight: "),
        dbc.Input(id="irweight", placeholder="Kg", type="number", disabled=True, value=0 ),
    ]
)


submitbtn = dbc.Button("Submit", id="submits", color="primary")
row1 = html.Tr([html.Td(submitbtn)])
table_body1 = [html.Tbody([row1])]
submitt = dbc.Table(table_body1, bordered=False)



DI = html.Div(
    [
        dbc.Row([
            dbc.Col(html.Div(" "), width=1),
            dbc.Col(html.Div(" "), width=1),
            dbc.Col(html.Div(" "), width=1),
        ]),
        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(manufacturerinput)),
                dbc.Col(html.Div(brandinput)),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col("Area"),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(areainput)),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(Weightinput)),
                dbc.Col(html.Div(Priceinput)),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(statusinput)),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(statusrecievedinput)),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(statusweightinput)),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(submitt)),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(" "), width=1),
            ]
        ),
    ]
),
inputt = html.Div(
        dbc.Row([
            dbc.Col(html.Div(" ")),
            dbc.Col(html.Div(DI),width=1),
            dbc.Col(html.Div(" ")),
        ]
        )
    )
#========================================================

content = html.Div(id="page-content", style=CONTENT_STYLE)
emp = html.Div(dbc.Row(html.Div("CURRENTLY NOT AVAILABLE!"),align="center"))
app.layout = html.Div([
    dcc.Location(id="url"), 
    navbar, 
    html.Div(" "),
    html.Div([
        dbc.Row(
            [
                dbc.Col(html.Div(" "), align="start", width=3),
                dbc.Col(html.Div("This program is just the prototype version of the actual program that the developers have imagined."), align="center", width=8),
                dbc.Col(html.Div(dcc.Interval(
                        id='interval-component',
                        interval = 10*1000,
                        n_intervals=0
                    ))),
                dbc.Col(html.Div(" "), align="end"),
            ],
            ),
        dbc.Row(
            dbc.Col(html.Div(id='live-update-time'))
        ),
        dbc.Row([
            dbc.Col(html.Div(DI),width=3),
            dbc.Col(html.Div(content),width=9),
        ])
    ]),
    dbc.Modal( #The modal that gave me headache. But its okay now.
        [
            dbc.ModalHeader("Success"),
            dbc.ModalBody("Transaction Successful!"),
            dbc.ModalFooter(
                dbc.Button("close",id="close")
            )
        ],
        id="modal",
    ),
    ])

@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):

    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    elif pathname == "/page-2":
        return False, True, False
    elif pathname == "/page-3":
        return False, False, True
    return [pathname == f"/page-{i}" for i in range(1, 4)]
#=============================================================================================
#=============================================================================================
@app.callback(
    [
        Output("modal","is_open"), 
        Output("istatus","value"), 
        Output("imanufacturer","value"), 
        Output("ibrand","value"), 
        Output("iarea","value"), 
        Output("iweight","value"), 
        Output("iprice","value"), 
        Output("irstatus","value"), 
        Output("irweight","value"),
    ],
    [
        Input("submits","n_clicks"), 
        Input("close","n_clicks"),
    ],
    [
        State("modal","is_open"),
        State("istatus","value"), 
        State("imanufacturer","value"), 
        State("ibrand","value"), 
        State("iarea","value"), 
        State("iweight","value"),
        State("iprice","value"), 
        State("irstatus","value"), 
        State("irweight","value"),
        State("istatus","invalid"), 
        State("imanufacturer","invalid"), 
        State("ibrand","invalid"), 
        State("iarea","invalid"), 
        State("iweight","invalid"),
        State("iprice","invalid"), 
        State("irstatus","invalid"), 
        State("irweight","invalid"),
    ]
    )
def toggle_modal(n1,n2,is_open, Status, Manufacturer, Brand, Area, Weight, Price, StatusRecieved, StatusWeight, valid1, valid2, valid3, valid4, valid5, valid6, valid7, valid8):
    dates = datetime.date.today()
    f"{dates.month:02d}" #format to keep the month double digit e.g. 01 for january
    f"{dates.day:02d}" #format to keep the day double digit e.g. 01
    datey = str(dates.year)
    datem = str(dates.month)
    dated = str(dates.day)
    Date = datey+datem+dated
    if (n1 is None): #or n2 is None or n3 is None):
        raise PreventUpdate #To prevent automatic update of the page
    elif n1:
        if (valid1 == True or valid2 == True or valid3 == True or valid4 == True or valid5 == True or valid6 == True or valid7 == True or valid8 == True):
            return None,'','','','','','','',''
        if (Manufacturer == '' or Brand == '' or Area == '' or Weight == '' or Price == '' or Status == ''):
            return None,'','','','','','','',''
        if (Manufacturer != None and Brand != None and Area != None and Weight != None and valid5 != True and Price != None and valid6 != True and Status != None and valid7 != True and valid8 != True): 
            if (StatusRecieved == "Complete"):
                StatusWeight = 0
            print("======================================================")
            print("Date Today : ", Date)
            print("Manufacturer: " + str(Manufacturer))
            print("Brand: " + str(Brand))
            print("Area: " + str(Area))
            print("Weight: " + str(Weight))
            print("Price: " + str(Price))
            print("Status: " + str(Status))
            print("Status Recieved : " + str(StatusRecieved))
            print("Status weight: " + str(StatusWeight))
            tx_hash = contract.functions.enterRiceInfo(str(Manufacturer), str(Brand), str(Area), str(Status), str(StatusRecieved), int(StatusWeight), int(Date), int(datey), int(datem), int(dated), int(Weight), int(Price)).transact()
            print("The Transaction hash is : ",web3.toHex(tx_hash))
            print("======================================================")
            return not is_open, '','','','','','','','' #Multiple returns for multiple Outputs
        else:
            return None,'','','','','','','',''
    elif n2:
        return not is_open,'','','','','','','',''
#==============================================================================================

@app.callback(
    [
        Output("irstatus","disabled"), 
        Output("istatus","invalid"),
    ],
    [
        Input("istatus","value"),
    ],
    [
        State("irstatus","disabled"), 
    ]
)
def recieved_status_input(val, is_abled):
    if val == "Recieved":
        return False, False
    if val == "Delivered":
        return True, False
    if val == None:
        return True, True
    else:
        return True, True
#===================================================================================
@app.callback(
    [
        Output("irweight","disabled"), 
        Output("irstatus", "invalid")
    ],
    [
        Input("irstatus","value"),
        Input("istatus","value"),
    ],
    [
        State("irweight","disabled"), 
        State("irstatus","invalid")
    ]
)
def recieved_weight_input(val, val2, is_abled, is_valid):
    if (val2 == "Recieved"):
        if val == "Damaged":
            return False, False
        elif val == "Complete":
            return True, False
        elif val == "Stolen":
            return False, False
        elif val == None:
            return False, True
        else:
            return True, True
    if (val2 == "Delivered"):
        return True, False
    else:
        return True, False
#=======================================================================================
@app.callback(
    Output("irweight","invalid"),
    [Input("irweight","value"), Input("irstatus", "value")],
    [State("irweight","invalid")]
)
def recieved_weight_input(val,val2, invalid):
    if (val2 == "Damaged" or val2 == "Stolen"):
        if val == '':
            return True
        if val == None:
            return True
        if val < 0 :
            return True
    if (val2 == None or val2 == "Complete"):
        return False
    else:
        return False
#==========================================
@app.callback(
    Output("imanufacturer","invalid"),
    [Input("imanufacturer","value")],
    [State("imanufacturer","invalid")]
)
def manufacturer_input(val, invalid):
    if (val == '' or val == None):
        return True
#==========================================
@app.callback(
    Output("ibrand","invalid"),
    [Input("ibrand","value")],
    [State("ibrand","invalid")]
)
def brand_input(val, invalid):
    if (val == '' or val == None):
        return True
#==========================================
@app.callback(
    Output("iarea","invalid"),
    [Input("iarea","value")],
    [State("iarea","invalid")]
)
def area_input(val, invalid):
    if (val == '' or val == None):
        return True
#==========================================
@app.callback(
    Output("iweight","invalid"),
    [Input("iweight","value")],
    [State("iweight","invalid")]
)
def weight_input(val, invalid):
    if (val == '' or val == None or val < 0):
        return True
#==========================================
@app.callback(
    Output("iprice","invalid"),
    [Input("iprice","value")],
    [State("iprice","invalid")]
)
def price_input(val, invalid):
    if (val == '' or val == None or val < 0):
        return True
#=============================================================================================
@app.callback(
        Output("page-content", "children"),
    [
        Input("url", "pathname")
    ],
    )
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return Graph2
    elif pathname == "/page-2":
        return Table1

    elif pathname == "/page-3":
        return Graph1

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
#=======================================================================
@app.callback(
    Output('live-update-time','children'),
    [Input('interval-component','n_intervals')]
)
def update_time(n):
    dates = datetime.date.today()
    f"{dates.month:02d}" #format to keep the month double digit e.g. 01 for january
    f"{dates.day:02d}" #format to keep the day double digit e.g. 01
    datey = str(dates.year)
    datem = str(dates.month)
    dated = str(dates.day)
    #print("O")
    return [
        html.Span('Date: {} {}, {}'.format(datem, dated, datey))
    ]

@app.callback(
    Output('live-update-date','figure'),
    [Input('interval-component','n_intervals')]
)
def update_time(n):
    loop = contract.functions.getTransID().call()
    limit = loop + 1
    dfall = pd.DataFrame()   # this is for all the rice info
    for i in range (1, int(limit)):
        stId = i
        manu = contract.functions.getManu(int(i)).call()
        bran = contract.functions.getBrand(int(i)).call()
        area = contract.functions.getArea(int(i)).call()
        stat = contract.functions.getStatus(int(i)).call() # Status (Delivered / Recieved)
        stRe = contract.functions.getStatusRecieved(int(i)).call()  # StatusRecieved (Damaged / Stolen / Complete)
        stWe = contract.functions.getStatusWeight(int(i)).call()  # StatusWeight (if stRe = Complete : stWe = 0)
        fuldate = str(contract.functions.getDate(int(i)).call())
        year = contract.functions.getYear(int(i)).call()
        mont = contract.functions.getMonth(int(i)).call()
        day = contract.functions.getDay(int(i)).call()
        wght = contract.functions.getWeight(int(i)).call()
        pric = contract.functions.getPrice(int(i)).call()

        if(stat == 'Delivered'):
            wght = wght*-1
        if(stRe == 'Stolen'):
            wght = wght-stWe
        elif(stRe == 'Damaged'):
            wght = wght-stWe

        rewg = wght-stWe # This is for the remaining weight
        s_datetime = datetime.datetime.strptime(fuldate, '%Y%m%d')
        Rice = {
            'Manufacturer': [manu],
            'Brand': [bran],
            'Area': [area],
            'Status': [stat],
            'StatusRecieved': [stRe],
            'StatusWeight': [stWe],
            'Date': [s_datetime],
            'Year': [year],
            'Month': [mont],
            'Day': [day],
            'Weight': [wght],
            'Price': [pric],
            'RemainingWeight': [rewg]
            }
        dfnew = pd.DataFrame(Rice, columns= ['Manufacturer', 'Brand', 'Area', 'Status', 'StatusRecieved', 'StatusWeight', 'Date', 'Year', 'Month', 'Day', 'Weight', 'Price', 'RemainingWeight'])
        dfall = dfall.append(dfnew, ignore_index=True)
    try:
        jan = int(dfall.loc[dfall['Month'] == 1,'Weight'].sum()) 
        feb = int(dfall.loc[dfall['Month'] == 2,'Weight'].sum()) 
        mar = int(dfall.loc[dfall['Month'] == 3,'Weight'].sum()) 
        apr = int(dfall.loc[dfall['Month'] == 4,'Weight'].sum()) 
        may = int(dfall.loc[dfall['Month'] == 5,'Weight'].sum()) 
        jun = int(dfall.loc[dfall['Month'] == 6,'Weight'].sum()) 
        jul = int(dfall.loc[dfall['Month'] == 7,'Weight'].sum()) 
        aug = int(dfall.loc[dfall['Month'] == 8,'Weight'].sum()) 
        sep = int(dfall.loc[dfall['Month'] == 9,'Weight'].sum()) 
        octo = int(dfall.loc[dfall['Month'] == 10,'Weight'].sum()) 
        nov = int(dfall.loc[dfall['Month'] == 11,'Weight'].sum()) 
        dec = int(dfall.loc[dfall['Month'] == 12,'Weight'].sum()) 
        print("Goods")
    except:
        jan = 0
        feb = 0
        mar = 0
        apr = 0
        may = 0
        jun = 0
        jul = 0
        aug = 0
        sep = 0
        octo = 0 
        nov = 0
        dec = 0
        print("Oh no!")
    Month = {
        'Months' : ['January', 'February','March','April','May','June','July','August','September','October','November','December'],
        'Weight' : [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]
    }
    dfmon = pd.DataFrame(Month, columns=['Weight','Months'])
    datefig = px.bar(dfmon, x="Months", y="Weight", title='Total Rice Weight / Date', color="Months", height=500)
    return datefig

@app.callback(
    Output('live-update-area','figure'),
    [Input('interval-component','n_intervals')]
)
def update_area(n):
    loop = contract.functions.getTransID().call()
    limit = loop + 1
    dfall = pd.DataFrame()   # this is for all the rice info
    for i in range (1, int(limit)):
        stId = i
        manu = contract.functions.getManu(int(i)).call()
        bran = contract.functions.getBrand(int(i)).call()
        area = contract.functions.getArea(int(i)).call()
        stat = contract.functions.getStatus(int(i)).call() # Status (Delivered / Recieved)
        stRe = contract.functions.getStatusRecieved(int(i)).call()  # StatusRecieved (Damaged / Stolen / Complete)
        stWe = contract.functions.getStatusWeight(int(i)).call()  # StatusWeight (if stRe = Complete : stWe = 0)
        fuldate = str(contract.functions.getDate(int(i)).call())
        year = contract.functions.getYear(int(i)).call()
        mont = contract.functions.getMonth(int(i)).call()
        day = contract.functions.getDay(int(i)).call()
        wght = contract.functions.getWeight(int(i)).call()
        pric = contract.functions.getPrice(int(i)).call()

        if(stat == 'Delivered'):
            wght = wght*-1
        if(stRe == 'Stolen'):
            wght = wght-stWe
        elif(stRe == 'Damaged'):
            wght = wght-stWe

        rewg = wght-stWe # This is for the remaining weight
        s_datetime = datetime.datetime.strptime(fuldate, '%Y%m%d')
        Rice = {
            'Manufacturer': [manu],
            'Brand': [bran],
            'Area': [area],
            'Status': [stat],
            'StatusRecieved': [stRe],
            'StatusWeight': [stWe],
            'Date': [s_datetime],
            'Year': [year],
            'Month': [mont],
            'Day': [day],
            'Weight': [wght],
            'Price': [pric],
            'RemainingWeight': [rewg]
            }
        dfnew = pd.DataFrame(Rice, columns= ['Manufacturer', 'Brand', 'Area', 'Status', 'StatusRecieved', 'StatusWeight', 'Date', 'Year', 'Month', 'Day', 'Weight', 'Price', 'RemainingWeight'])
        dfall = dfall.append(dfnew, ignore_index=True)
    try:
        ohl = int(dfall.loc[dfall['Area'] == 'old hermitland','Weight'].sum()) 
        nhl = int(dfall.loc[dfall['Area'] == 'new hermitland','Weight'].sum()) 
        sd = int(dfall.loc[dfall['Area'] == 'shopping district', 'Weight'].sum()) 
    except:
        ohl = 0
        nhl = 0
        sd = 0

    Location = {
        'Location' : ['old hermitland', 'new hermitland', 'shopping district',],
        'Weight' : [ohl, nhl, sd]
    }

    dfloc = pd.DataFrame(Location,columns=['Weight',  'Location'])
    barfig = px.bar(dfloc, x="Location", y="Weight", title='Total Rice Weight / Region', color="Location", height=500)
    return barfig

#=======================================================================

@app.callback(
    Output('live-update-table','figure'),
    [Input('interval-component','n_intervals')]
)

def update_tabble(n):
    loop = contract.functions.getTransID().call()
    limit = loop + 1
    dfall = pd.DataFrame()   # this is for all the rice info
    for i in range (1, int(limit)):
        stId = i
        manu = contract.functions.getManu(int(i)).call()
        bran = contract.functions.getBrand(int(i)).call()
        area = contract.functions.getArea(int(i)).call()
        stat = contract.functions.getStatus(int(i)).call() # Status (Delivered / Recieved)
        stRe = contract.functions.getStatusRecieved(int(i)).call()  # StatusRecieved (Damaged / Stolen / Complete)
        stWe = contract.functions.getStatusWeight(int(i)).call()  # StatusWeight (if stRe = Complete : stWe = 0)
        fuldate = str(contract.functions.getDate(int(i)).call())
        year = contract.functions.getYear(int(i)).call()
        mont = contract.functions.getMonth(int(i)).call()
        day = contract.functions.getDay(int(i)).call()
        wght = contract.functions.getWeight(int(i)).call()
        pric = contract.functions.getPrice(int(i)).call()

        if(stat == 'Delivered'):
            wght = wght*-1
        if(stRe == 'Stolen'):
            wght = wght-stWe
        elif(stRe == 'Damaged'):
            wght = wght-stWe

        rewg = wght-stWe # This is for the remaining weight
        s_datetime = datetime.datetime.strptime(fuldate, '%Y%m%d')
        Rice = {
            'Manufacturer': [manu],
            'Brand': [bran],
            'Area': [area],
            'Status': [stat],
            'StatusRecieved': [stRe],
            'StatusWeight': [stWe],
            'Date': [s_datetime],
            'Year': [year],
            'Month': [mont],
            'Day': [day],
            'Weight': [wght],
            'Price': [pric],
            'RemainingWeight': [rewg]
            }
        dfnew = pd.DataFrame(Rice, columns= ['Manufacturer', 'Brand', 'Area', 'Status', 'StatusRecieved', 'StatusWeight', 'Date', 'Year', 'Month', 'Day', 'Weight', 'Price', 'RemainingWeight'])
        dfall = dfall.append(dfnew, ignore_index=True)
    try:
        tablefig = go.Figure(data=[go.Table(
            header=dict(
                values=['<b>Date</b>','<b>Area</b>','<b>Manufacturer</b>','<b>Brand</b>','<b>Status</b>','<b>Damaged, Stolen, Complete</b>','<b>Weight(kg)</b>','<b>Weight of Damage</b>','<b>Usable/Sellable Rice(kg)</b>','<b>Price per kg</b>'],
                line_color='darkslategray',
                align=['center'],
                font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[
                    dfall.Date,
                    dfall.Area,
                    dfall.Manufacturer,
                    dfall.Brand,
                    dfall.Status,
                    dfall.StatusRecieved,
                    dfall.Weight,
                    dfall.StatusWeight,
                    dfall.RemainingWeight,
                    dfall.Price
                    ],
                line_color='darkslategray',
                align = ['center'],
                font = dict(color = 'darkslategray', size = 12),
            ))
        ])
    except:
            tablefig = go.Figure(data=[go.Table(
            header=dict(
                values=['<b>Date</b>','<b>Area</b>','<b>Manufacturer</b>','<b>Brand</b>','<b>Status</b>','<b>Damaged, Stolen, Complete</b>','<b>Weight(kg)</b>','<b>Weight of Damage</b>','<b>Usable/Sellable Rice(kg)</b>','<b>Price per kg</b>'],
                line_color='darkslategray',
                align=['center'],
                font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None
                    ],
                line_color='darkslategray',
                align = ['center'],
                font = dict(color = 'darkslategray', size = 12),
            ))
        ])
    return tablefig
#=======================================================================
if __name__ == '__main__':
    app.run_server(debug=True)

