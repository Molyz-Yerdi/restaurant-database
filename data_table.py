import sqlite3


# Таблицы
def GetData_Clients():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Clients'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2], i[3], i[4], i[5]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Clients(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Clients VALUES (NULL, ?, ?, ?, ?, ?)'
        cursor.execute(query, lst)


def GetData_Staff():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Staff'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Staff(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Staff VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(query, lst)


def GetData_Compositions():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Compositions'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Compositions(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Compositions VALUES (NULL, ?, ?)'
        cursor.execute(query, lst)


def GetData_Contacts():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Contacts'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2], i[3], i[4]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Contacts(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Contacts VALUES (NULL, ?, ?, ?, ?)'
        cursor.execute(query, lst)


def GetData_DiscProm():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM DiscProm'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2], i[3]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_DiscProm(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO DiscProm VALUES (NULL, ?, ?, ?)'
        cursor.execute(query, lst)


def GetData_Menu():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Menu'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2], i[3]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Menu(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Menu VALUES (NULL, ?, ?, ?)'
        cursor.execute(query, lst)


def GetData_Orders():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Orders'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2], i[3]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Orders(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Orders VALUES (NULL, ?, ?, ?)'
        cursor.execute(query, lst)


def GetData_Recipes():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Recipes'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Recipes(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Recipes VALUES (NULL, ?, ?)'
        cursor.execute(query, lst)


def GetData_Schedule():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Schedule'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2], i[3], i[4]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Schedule(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Schedule VALUES (NULL, ?, ?, ?, ?)'
        cursor.execute(query, lst)


def GetData_Warehouse():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM Warehouse'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2], i[3], i[4]))
        #for i in all_data:
            #print(i)
    return(all_data)

def InsertData_Warehouse(lst):
    with sqlite3.connect('rest.db') as db:
        cursor = db.cursor()
        query = 'INSERT INTO Warehouse VALUES (NULL, ?, ?, ?, ?)'
        cursor.execute(query, lst)




# Представления
def GetData_client_exp():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM client_exp'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1], i[2]))
        #for i in all_data:
            #print(i)
    return(all_data)


def GetData_inventory():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM inventory'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1]))
        #for i in all_data:
            #print(i)
    return(all_data)


def GetData_sales():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM sales'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1]))
        #for i in all_data:
            #print(i)
    return(all_data)


def GetData_statistic():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM statistic'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1]))
        #for i in all_data:
            #print(i)
    return(all_data)


def GetData_summator():
    all_data = []
    with sqlite3.connect('rest.db') as db:
        db.row_factory = sqlite3.Row
        #db.row_factory = dict_factory
        cursor = db.cursor()
        query = 'SELECT * FROM summator'
        cursor.execute(query)
        for i in cursor:
            all_data.append((i[0], i[1]))
        #for i in all_data:
            #print(i)
    return(all_data)
