import sqlite3 as sq

with sq.connect('rest.db') as con:
    cur = con.cursor()

    # Запросы для создания таблиц
    query_staff = '''
    CREATE TABLE IF NOT EXISTS Staff
    (
    id_staffer INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex TEXT NOT NULL,
    post TEXT NOT NULL,
    salary INTEGER NOT NULL,
    passport_series TEXT NOT NULL,
    passport_number TEXT NOT NULL,
    datebirth TEXT NOT NULL,
    phonenumber TEXT NOT NULL,
    email TEXT NOT NULL,
    date_emp TEXT
    )
    '''

    query_clients = '''
    CREATE TABLE IF NOT EXISTS Clients
    (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex TEXT,
    datebirth TEXT,
    phonenumber TEXT,
    email TEXT
    )
    '''

    query_warehouse = '''
    CREATE TABLE IF NOT EXISTS Warehouse
    (
    id_ingred INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ingred TEXT NOT NULL,
    price INTEGER NOT NULL,
    delivery_date TEXT,
    expiration_date TEXT NOT NULL
    )
    '''

    query_schedule = '''
    CREATE TABLE IF NOT EXISTS Schedule
    (
    is_sch INTEGER PRIMARY KEY AUTOINCREMENT,
    id_staffer INTEGER NOT NULL,
    weekday TEXT NOT NULL,
    bwgwd TEXT NOT NULL,
    endwd TEXT NOT NULL,

    FOREIGN KEY (id_staffer) REFERENCES Staff(id_staffer) ON DELETE CASCADE
    )
    '''

    query_menu = '''
    CREATE TABLE IF NOT EXISTS Menu
    (
    id_pizza INTEGER PRIMARY KEY AUTOINCREMENT,
    pizza_name TEXT NOT NULL,
    price INTEGER,
    coocking_time TEXT NOT NULL
    )
    '''

    query_recipes = '''
    CREATE TABLE IF NOT EXISTS Recipes
    (
    id_recipe INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pizza INTEGER NOT NULL,
    id_ingred INTEGER NOT NULL,

    FOREIGN KEY (id_pizza) REFERENCES Menu(id_pizza) ON DELETE CASCADE
    FOREIGN KEY (id_ingred) REFERENCES Warehouse(id_ingred) ON DELETE CASCADE
    )
    '''

    query_orders = '''
    CREATE TABLE IF NOT EXISTS Orders
    (
    id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    date_order TEXT NOT NULL,
    id_staffer INTEGER NOT NULL,
    id_client INTEGER NOT NULL,

    FOREIGN KEY (id_staffer) REFERENCES Staff(id_staffer) ON DELETE CASCADE,
    FOREIGN KEY (id_client) REFERENCES Clients(id_client) ON DELETE CASCADE
    )
    '''

    query_compositions = '''
    CREATE TABLE IF NOT EXISTS  Compositions
    (
    id_comp INTEGER PRIMARY KEY AUTOINCREMENT,
    id_order INTEGER NOT NULL,
    id_pizza INTEGER NOT NULL,

    FOREIGN KEY (id_order) REFERENCES Orders(id_order),
    FOREIGN KEY (id_pizza) REFERENCES Menu(id_pizza)
    )
    '''

    query_discprom = '''
    CREATE TABLE IF NOT EXISTS DiscProm
    (
    id_diskprom INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pizza INTEGER NOT NULL,
    description TEXT NOT NULL,
    date TEXT NOT NULL,

    FOREIGN KEY (id_pizza) REFERENCES Menu(id_pizza) ON DELETE CASCADE
    )
    '''

    query_contacts = '''
    CREATE TABLE IF NOT EXISTS Contacts
    (
    id_contacts INTEGER PRIMARY KEY AUTOINCREMENT,
    manager INTEGER NOT NULL,
    adress TEXT NOT NULL,
    phonenumber TEXT NOT NULL,
    email TEXT NOT NULL,

    FOREIGN KEY (manager) REFERENCES Staff(id_staffer) ON DELETE CASCADE
    )
    '''




    # Запросы для создания представлений
    query_inventory = '''
    CREATE VIEW IF NOT EXISTS inventory AS
    SELECT w.name_ingred,
           count(w.name_ingred)
    FROM Warehouse AS w
    GROUP BY w.name_ingred
    '''

    query_sales = '''
    CREATE VIEW IF NOT EXISTS sales AS
    SELECT c.id_pizza,
           count(c.id_pizza)
    FROM Compositions AS c
    GROUP BY c.id_pizza
    '''

    query_statistic = '''
    CREATE VIEW IF NOT EXISTS statistic AS
    SELECT o.date_order,
           count(o.id_order)
    FROM Orders AS o
    GROUP BY o.date_order
    '''

    query_client_exp = '''
    CREATE VIEW IF NOT EXISTS client_exp AS
    SELECT Orders.id_client, Compositions.id_order,
    	   Compositions.id_pizza, Menu.price
    FROM Orders LEFT JOIN Compositions
    ON Orders.id_order = Compositions.id_order
    LEFT JOIN Menu ON Compositions.id_pizza = Menu.id_pizza
    ORDER BY Orders.id_client
    '''

    query_summator = '''
    CREATE VIEW IF NOT EXISTS summator AS
        SELECT id_order, sum(price) AS sum
        FROM client_exp
        GROUP BY id_order
        ORDER BY id_order
    '''


    # Запросы на создание триггеров
    query_date_staff = '''
    CREATE TRIGGER IF NOT EXISTS date_staff AFTER INSERT ON Staff
    BEGIN

        UPDATE Staff SET date_emp = date('now') WHERE id_staffer == NEW.id_staffer;
    END;
    '''

    query_adeq_prs = '''
    CREATE TRIGGER IF NOT EXISTS adeq_prs AFTER INSERT ON Menu
    BEGIN
        SELECT CASE WHEN NEW.price <= 0 THEN
            RAISE(ABORT, 'Invalid Quantity')
        END;
    END;
    '''

    query_date_ware = '''
    CREATE TRIGGER IF NOT EXISTS date_ware AFTER INSERT ON Warehouse
    BEGIN
        UPDATE Warehouse SET delivery_date = date('now') WHERE id_ingred == NEW.id_ingred;
    END;
    '''

    query_date_order = '''
    CREATE TRIGGER IF NOT EXISTS date_order AFTER INSERT ON Orders
    BEGIN
        UPDATE Orders SET date_order = date('now') WHERE id_order == NEW.id_order;
    END;
    '''



    # Создаем таблицы
    cur.execute(query_staff)
    cur.execute(query_clients)
    cur.execute(query_warehouse)
    cur.execute(query_schedule)
    cur.execute(query_menu)
    cur.execute(query_recipes)
    cur.execute(query_orders)
    cur.execute(query_contacts)
    cur.execute(query_compositions)
    cur.execute(query_discprom)

    # Создаем представления
    cur.execute(query_inventory)
    cur.execute(query_sales)
    cur.execute(query_statistic)
    cur.execute(query_client_exp)
    cur.execute(query_summator)

    # Создаем триггеры
    cur.execute(query_date_staff)
    cur.execute(query_adeq_prs)
    cur.execute(query_date_ware)
    cur.execute(query_date_order)
