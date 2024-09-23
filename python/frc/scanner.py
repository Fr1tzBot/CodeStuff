import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SHEET_ID = "1ZjxDvhhqDU_ToltdoWwzmiqc43aSAlOVWazK18OCino"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

DATABASE = "./database.csv"
RANGE = "inventory!A2:H"

#auth stuff

creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
# Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())

#database format:
#Barcode, Stock Level, Image, Name, Category, Description, Quantity, Container

class Item:
    def __init__(self, *args):
        if len(args) == 0:
            self.code = ""
            self.stockLevel = ""
            self.image = ""
            self.name = ""
            self.category = ""
            self.description = ""
            self.quantity = ""
            self.container = ""
            return
        elif len(args) == 8:
            self.code = args[0]
            self.stockLevel = args[1]
            self.image = args[2]
            self.name = args[3]
            self.category = args[4]
            self.description = args[5]
            self.quantity = args[6]
            self.container = args[7]
        elif len(args) == 6:
            self.code = args[0]
            self.stockLevel = ""
            self.image = ""
            self.name = args[1]
            self.category = args[2]
            self.description = args[3]
            self.quantity = args[4]
            self.container = args[5]
        else:
            raise TypeError("Invalid number of arguments")

    def __str__(self):
        return f"Barcode: {self.code}\nName: {self.name}\nCategory: {self.category}\nDescription: {self.description}\nQuantity: {self.quantity}\nContainer: {self.container}"

    def __repr__(self):
        return f"Item({self.code}, {self.name}, {self.category}, {self.description}, {self.quantity}, {self.container})"

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)

def checkCode(code: str) -> bool:
    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SHEET_ID, range=RANGE)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return False
        
        for i in values:
            if code == str(i[0]):
                return True
    except HttpError as err:
        print(err)
    return False
            
def addItem(item: Item) -> None:
    #add item to database
    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .append(
                spreadsheetId=SHEET_ID,
                range=RANGE,
                valueInputOption="USER_ENTERED",
                body={"values": [[item.code, item.stockLevel, item.image, item.name, item.category, item.description, item.quantity, item.container]]},
            )
            .execute()
        )
    except HttpError as err:
        print(err)

def readItem(code: str) -> Item:
    #get item info from database
    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SHEET_ID, range=RANGE)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return Item()

        for i in values:
            if code == i[0]:
                return Item(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
    except HttpError as err:
        print(err)

def setQty(code: str, qty: int) -> None:
    #set quantity of item
    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SHEET_ID, range=RANGE)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        for i in values:
            if code == i[0]:
                i[6] = qty
                break
        else:
            print("Item not found in database")
            return

        result = (
            sheet.values()
            .update(
                spreadsheetId=SHEET_ID,
                range=RANGE,
                valueInputOption="USER_ENTERED",
                body={"values": values},
            )
            .execute()
        )
    except HttpError as err:
        print(err)
while True:
    code = input("Awaiting scan... (Press enter to exit) ")

    code = code.strip()
    #remaining code will only run when a code is scanned

    if code == "exit" or code is None or code == "" : #filter out invalid inputs
        print("Exiting...")
        break

    #remove leading zeros
    while code[0] == "0":
        code = code[1:]

    if checkCode(code):
        print("Item found!")
        item = readItem(code)
        print(item)
        qty = input("Enter new quantity: ")
        if qty[0] == "+":
            qty = str(int(qty[1:]) + int(item.quantity))
        elif qty[0] == "-":
            qty = str(int(item.quantity) - int(qty[1:]))
        setQty(code, str(int(qty)))
    else:
        print("Item not found in database")
        name = input("Enter name: ")
        if name == code:
            print("Double scan detected")
            continue
        category = input("Enter category: ")
        description = input("Enter description: ")
        quantity = int(input("Enter quantity: "))
        container = input("Enter container: ")
        if "" in [name, category, description, quantity, container]:
            print("Invalid input")
            continue
        #add item to database
        addItem(Item(code, name, category, description, quantity, container))
        print("Item added to database")
