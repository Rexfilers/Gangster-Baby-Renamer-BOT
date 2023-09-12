import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11792434")

API_HASH = os.environ.get("API_HASH", "01e88901122505e544f89ac04540063e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6479602205:AAEUmelbKtDT0F8pxw10wndDiCZ0RTFK3uA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MOVIES_PROVIDE") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://mikoxa5747:1234@cluster0.nzu6dcg.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/0d9a268d4abb5566551b1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
