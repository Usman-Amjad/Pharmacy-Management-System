import sqlite3


def pharmacyDb():
    con = sqlite3.connect(database=r'hpd.db')
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender TEXT,"
        "contact TEXT,dob TEXT,doj TEXT,pass TEXT,utype TEXT,address TEXT,salary TEXT)")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT,"
        "name TEXT, scheme TEXT, price INTEGER, sellingPrice INTEGER, qty INTEGER, totalPrice INTEGER, status TEXT, location TEXT)")

    cur.execute('''CREATE TABLE IF NOT EXISTS sellDetails(item_id INTEGER,'''
                '''name TEXT, price INTEGER, qty INTEGER, totalPrice INTEGER, sellerName TEXT, location TEXT, discount INTEGER, netPay INTEGER, sellDate TEXT);''')

    cur.execute(
        "CREATE TABLE IF NOT EXISTS productDetails(pid INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT,"
        "name TEXT, scheme TEXT, price INTEGER, sellingPrice INTEGER, qty INTEGER, totalPrice INTEGER, status TEXT, location TEXT, Date TEXT, Time, TEXT)")

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS returnedItems(item_id INTEGER, category TEXT, item_name TEXT, item_price INTEGER
                                                , item_qty INTEGER, item_totalPrice INTEGER, item_returnDate TEXT);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS orders(orderId INTEGER, pid INTEGER, orderItemName TEXT, perItemPrice FLOAT
                                                        , orderQty INTEGER, orderTotalPrice FLOAT, orderStatus TEXT
                                                        , orderDiscount FLOAT, orderNetPrice FLOAT, orderPayType TEXT
                                                        , orderCustomerName TEXT, orderCustomerPhone TEXT, orderDate TEXT
                                                        , orderTime TEXT, FOREIGN KEY (pid) REFERENCES product(pid))''')

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS returnedOrders(orderId INTEGER, orderItemName TEXT, perItemPrice FLOAT, orderQty INTEGER
                                                    , orderTotalPrice FLOAT, orderStatus TEXT, orderDiscount FLOAT
                                                    , orderNetPrice FLOAT, orderPayType TEXT, orderCustomerName TEXT
                                                    , orderCustomerPhone TEXT, orderDate TEXT, orderTime TEXT);''')

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS customersDetails(custId INTEGER PRIMARY KEY, custName TEXT, custBalance INTEGER, custStatus TEXT);''')

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS custPaymentDetails(custId INTEGER, custName TEXT, custBalance INTEGER, custPaid INTEGER
                                                        , custTotalBalance INTEGER, custPayType TEXT, custPayDate TEXT, custStatus TEXT);''')

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS shopExpensesNames(expID INTEGER PRIMARY KEY AUTOINCREMENT, expDesc TEXT);''')

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS shopExpenses(expID INTEGER PRIMARY KEY AUTOINCREMENT, expDesc TEXT, expPrice INTEGER, expDate TEXT);''')

    con.commit()
    con.close()

pharmacyDb()


# cur.execute("CREATE TABLE IF NOT EXISTS prescriptions( id INTEGER PRIMARY KEY, patient_name TEXT, medication_name TEXT, dosage TEXT, refill_date DATE, prescribing_physician TEXT, allergies TEXT )")
# cur.execute("CREATE TABLE IF NOT EXISTS inventory( id INTEGER PRIMARY KEY, product_name TEXT, quantity INTEGER, threshold INTEGER)")
# cur.execute("CREATE TABLE IF NOT EXISTS sales( id INTEGER PRIMARY KEY, product_name TEXT, quantity INTEGER, price REAL, timestamp DATETIME) ")
# cur.execute("CREATE TABLE IF NOT EXISTS customers( id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT )")
