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
from random import randint # for random integer value
from dash.dependencies import Input, Output, State
from datetime import date, timedelta # to get date today
from web3 import Web3
from dash.exceptions import PreventUpdate
#========================================================

# Stylish stuff here
#========================================================
app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO], suppress_callback_exceptions=True)

CONTENT_STYLE = {
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


# Blockchain stuff here
#========================================================

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]


abi = json.loads('[{"inputs":[{"internalType":"string","name":"_UserName","type":"string"}],"name":"Login","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_UserName","type":"string"},{"internalType":"string","name":"_Password","type":"string"}],"name":"Register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_Manufacturer","type":"string"},{"internalType":"string","name":"_Brand","type":"string"},{"internalType":"string","name":"_Area","type":"string"},{"internalType":"string","name":"_Status","type":"string"},{"internalType":"string","name":"_StatusRecieved","type":"string"},{"internalType":"uint256","name":"_StatusWeight","type":"uint256"},{"internalType":"uint256","name":"_Date","type":"uint256"},{"internalType":"uint256","name":"_Year","type":"uint256"},{"internalType":"uint256","name":"_Month","type":"uint256"},{"internalType":"uint256","name":"_Day","type":"uint256"},{"internalType":"uint256","name":"_Weight","type":"uint256"},{"internalType":"uint256","name":"_Price","type":"uint256"}],"name":"enterRiceInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getArea","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getBrand","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getManu","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getMonth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatus","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusRecieved","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTransID","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getYear","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"newcount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"transactionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

# needs to be changed to match address in remix solidity
address = web3.toChecksumAddress("0x921db743c34cA00d6d8dcB0A1f08f23e0b204E51")

contract = web3.eth.contract(address=address, abi=abi)

loop = contract.functions.getTransID().call()
limit = loop + 1

# this is the dataframwe
dfall = pd.DataFrame()   # this is for all the rice info
#dftest = pd.read_excel('testarea.xlsx') # this is for all the cities in ph

# Backend stuff
#========================================================
# this is what calls all data and adds it to the dataframe
#========================================================
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
            }

    dfnew = pd.DataFrame(Rice, columns= ['Manufacturer', 'Brand', 'Area', 'Status', 'StatusRecieved', 'StatusWeight', 'Date', 'Year', 'Month', 'Day', 'Weight'])
    dfall = dfall.append(dfnew, ignore_index=True)



# creates a dataframe for the bar graph
#========================================================

ohl = int(dfall.loc[dfall['Area'] == 'old hermitland', 'Weight'].sum())
nhl = int(dfall.loc[dfall['Area'] == 'new hermitland', 'Weight'].sum())
sd = int(dfall.loc[dfall['Area'] == 'shopping district', 'Weight'].sum())

Location = {
    'Location' : ['old hermitland', 'new hermitland', 'shopping district',],
    'Weight' : [ohl, nhl, sd]
}

dfloc = pd.DataFrame(Location,columns=['Weight',  'Location'])


# Table Stuff
#========================================================
tablefig = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Date</b>','<b>Area</b>','<b>Manufacturer</b>','<b>Brand</b>','<b>Weight(kg)</b>','<b>Status</b>','<b>Damaged, Stolen, Complete</b>','<b>Weight of Damage</b>'],
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
            dfall.Weight,
            dfall.Status,
            dfall.StatusRecieved,
            dfall.StatusWeight
            ],
        line_color='darkslategray',
        align = ['center'],
        font = dict(color = 'darkslategray', size = 12),
    ))
])
#========================================================

#========================================================
barfig = px.bar(dfloc, x="Location", y="Weight", title='Total Rice Weight / Region', color="Location", height=500)
#========================================================
#datefic = px.bar(dfloc, x="")

# Webpage stuff
#========================================================
# Navbar
#========================================================
navbar = dbc.NavbarSimple(
    children = [
        dbc.NavItem(dbc.NavLink("GRAPHS", href="/page-1", id="page-1-link")),
	    dbc.NavItem(dbc.NavLink("TABLES", href="/page-2", id="page-2-link")),
	    dbc.NavItem(dbc.NavLink("INPUT", href="/page-3", id="page-3-link")),
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
                    dbc.Col(html.Div(dcc.Graph(figure = barfig))),
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
                dbc.Col(html.Div(dcc.Graph(figure = tablefig))),
                #dbc.Col(html.Div(" "), width=1),
            ]
        ),
    ]
)
#========================================================
# Data Input
#========================================================
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
                {"label": "Damaged", "value": 1},
                {"label": "Complete", "value": 2},
                {"label": "Stolen", "value": 3},
            ], 
            value = 2,
            disabled = True
    ),
])
                    

statusweightinput = dbc.FormGroup( #status recieved weight input
    [
        dbc.Label("Status Weight: "),
        dbc.Input(id="irweight", placeholder="Kg", type="number", disabled=True),
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
                dbc.Col("Status"),
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
                dbc.Col(html.Div(" "), align="end"),
            ],
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
    )
    ])

@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]
#=============================================================================================INPUT
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
    ]
    )
def toggle_modal(n1,n2,is_open, Status, Manufacturer, Brand, Area, Weight, Price, StatusRecieved, StatusWeight):
    dates = datetime.date.today()
    f"{dates.month:02d}" #format to keep the month double digit e.g. 01 for january
    f"{dates.day:02d}" #format to keep the day double digit e.g. 01
    datey = str(dates.year)
    datem = str(dates.month)
    dated = str(dates.day)
    Date = datey+datem+dated
    if n1 is None:
        raise PreventUpdate #To prevent automatic update of the page
    if n1:
        if Manufacturer != '': #not yet done. Planning to optimize if statement so that all input is correctly filled
            print("======================================================")
            print("Manufacturer: " + str(Manufacturer))
            print("Brand: " + str(Brand))
            print("Area: " + str(Area))
            print("Weight: " + str(Weight))
            print("Price: " + str(Price))
            print("Status: " + str(Status))
            print("Status Recieved : " + str(StatusRecieved))
            print("Status weight: " + str(StatusWeight))
            print("Date Today : ", Date)
            tx_hash = contract.functions.enterRiceInfo(str(Manufacturer), str(Brand), str(Area), str(Status), str(StatusRecieved), int(StatusWeight), int(Date), int(datey), int(datem), int(dated), int(Weight), int(Price)).transact()
            print("The Transaction hash is : ",web3.toHex(tx_hash))
            print("======================================================")
            return not is_open,'','','','','','','','' #Multiple returns for multiple Outputs
    if n2:
        if n1 is None:
            raise PreventUpdate #Don't really know or feel the difference if I remove this
        return not is_open,'','','','','','','',''
#==============================================================================================

#===============================================================================================
@app.callback( #Callback to automatically update input for Recieved Status
    Output("irstatus","disabled",),
    [Input("istatus","value")],
    [State("irstatus","disabled")]
)
def on_form_change(val, is_open):
    if val == "Delivered":
        return True
    if val == "Recieved":
        return False
    if val == '':
        return True
#=========================================================================
@app.callback( #Callback to automatically update input for Recieved Weight Status
    Output("irweight","disabled",),
    [Input("istatus","value")],
    [State("irweight","disabled")]
)
def on_form_change(val2, is_open):
    if val2 == "Delivered":
        return True
    if val2 == "Recieved":
        return False
    if val2 == '':
        return True
    #if status == 3:
    #    return True
        
#=============================================================================================
@app.callback(
    Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return Graph1

    elif pathname == "/page-2":
        return Table1

    elif pathname == "/page-3":
        return emp

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
#=======================================================================

#=======================================================================
if __name__ == '__main__':
    app.run_server(debug=True)

