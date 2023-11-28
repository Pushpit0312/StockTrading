read latest data from market data
randomly increse or decrease prices
insert data in stock price history
import connection

# Database details
HOST = ""
PORT = 3307
USERNAME = "root"
PASSWORD = "root"
DATABASE = "pvs_stock_trading"

# Connecting to database and creating the database:
conn = connection.create_connection(USERNAME, PASSWORD, HOST, PORT)