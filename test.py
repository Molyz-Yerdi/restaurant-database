from tkinter import *                                                           # Импортируем все необходимые библиотеки
from tkinter import ttk
import sqlite3
from data_table import *                                                        # Импортируем файл с функциями запросов к базе
from tkcalendar import DateEntry, Calendar
from tkinter import messagebox
#import os

#os.system('python authorization.py')

# главное окно приложения
window = Tk()
# заголовок окна
window.title('Авторизация')
# размер окна
window.geometry('450x230+650+250')
# можно ли изменять размер окна - нет
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

role = 'None'
# обработчик нажатия на клавишу 'Войти'
def clicked():
    global role
    # получаем имя пользователя и пароль
    username = username_entry.get()
    password = password_entry.get()

    if username == 'Admin' and password == 'qwerty':
        #print('Admin')
        window.destroy()
        role = 'Admin'
    elif username == 'Waiter' and password == 'qwerty':
        #print('Waiter')
        window.destroy()
        role = 'Waiter'
    elif username == 'Cook' and password == 'qwerty':
        #print('Cook')
        window.destroy()
        role = 'Cook'
    elif username == 'Guest' and password == 'qwerty':
        #print('Guest')
        window.destroy()
        role = 'Guest'
    else:
        messagebox.showinfo('Ошибка авторизации', 'Неверно введен логин или пароль')


# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# для всех остальных виджетов настройки делаются также
main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
main_label.pack()

# метка для поля ввода имени
username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
username_label.pack()

# поле ввода имени
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# метка для поля ввода пароля
password_label = Label(window, text='Пароль', font=label_font , **base_padding)
password_label.pack()

# поле ввода пароля
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry, show='*')
password_entry.pack()

# кнопка отправки формы
send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)


# запускаем главный цикл окна
window.mainloop()


win = Tk()                                                                      # Настраиваем параметры окна
photo = PhotoImage(file = 'static/pizza_icon.png')
win.iconphoto(False, photo)
win.title('База данных')
#win.geometry('1550x645+100+100')
#win.resizable(False, False)

if role == 'None':
    win.destroy()

# Блок кода, отвечающий за форму ввода
def ClearEntry():                                                               # Фнукция очищения полей формы ввода
    clear_entry = [
    entry_name,
    entry_sex,
    entry_datebirth,
    entry_phonenumber,
    entry_email,
    entry_id_order_comp,
    entry_id_pizza_comp,
    entry_manager_cont,
    entry_adress_cont,
    entry_phonenumber_cont,
    entry_email_cont,
    entry_id_pizza_dp,
    entry_description_dp,
    entry_date_dp,
    entry_pizza_name_menu,
    entry_price_menu,
    entry_coocking_time_menu,
    entry_date_order_ord,
    entry_id_staffer_ord,
    entry_id_client_ord,
    entry_id_pizza_rec,
    entry_id_ingred_rec,
    entry_id_stuffer_sch,
    entry_weekday_sch,
    entry_bwgwd_sch,
    entry_endwd_sch,
    entry_name_ingred_wh,
    entry_price_wh,
    entry_delivery_date_wh,
    entry_expiration_date_wh
                  ]
    for object_name in clear_entry:
        object_name.delete("0", END)


def BtnEnter():                                                                 # Функция ввода данных в базу
    if combo_tables.get() == 'Clients':
        name = entry_name.get()
        sex = entry_sex.get()
        datebirth = entry_datebirth.get()
        phonenumber = entry_phonenumber.get()
        email = entry_email.get()
        InsertData_Clients([name, sex, datebirth, phonenumber, email])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'Compositions':
        InsertData_Compositions([entry_id_order_comp.get(), entry_id_pizza_comp.get()])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'Contacts':
        InsertData_Contacts([entry_manager_cont.get(),
                            entry_adress_cont.get(),
                            entry_phonenumber_cont.get(),
                            entry_email_cont.get()])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'DiscProm':
        InsertData_DiscProm([entry_id_pizza_dp.get(),
                            entry_description_dp.get(),
                            entry_date_dp.get()])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'Menu':
        InsertData_Menu([entry_pizza_name_menu.get(),
                            entry_price_menu.get(),
                            entry_coocking_time_menu.get()])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'Orders':
        InsertData_Orders([entry_date_order_ord.get(),
                            entry_id_staffer_ord.get(),
                            entry_id_client_ord.get()])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'Recipes':
        InsertData_Recipes([entry_id_pizza_rec.get(),
                            entry_id_ingred_rec.get()])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'Schedule':
        InsertData_Schedule([entry_id_stuffer_sch.get(),
                            entry_weekday_sch.get(),
                            entry_bwgwd_sch.get(),
                            entry_endwd_sch.get()])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'Staff':
        InsertData_Staff([entry_name_staff.get(),
                            entry_sex_staff.get(),
                            entry_post.get(),
                            entry_salary.get(),
                            entry_passport_series.get(),
                            entry_passport_number.get(),
                            entry_datebirth_staff.get(),
                            entry_phonenumber.get(),
                            entry_email_staff.get(),
                            entry_date_emp.get()])
        ClearEntry()
        TablesTables()

    if combo_tables.get() == 'Warehouse':
        InsertData_Warehouse([entry_name_ingred_wh.get(),
                            entry_price_wh.get(),
                            entry_delivery_date_wh.get(),
                            entry_expiration_date_wh.get()])
        ClearEntry()
        TablesTables()




# Функция удаления виджетов в окне
def DeleteAll():
    destroy_object = [
    name,
    sex,
    datebirth,
    phonenumber,
    email,
    entry_name,
    entry_sex,
    entry_datebirth,
    entry_phonenumber,
    entry_email,
    name_staff,
    sex_staff,
    post,
    salary,
    passport_series,
    passport_number,
    datebirth_staff,
    phonenumber,
    email_staff,
    date_emp,
    entry_name_staff,
    entry_sex_staff,
    entry_post,
    entry_salary,
    entry_passport_series,
    entry_passport_number,
    entry_datebirth_staff,
    entry_phonenumber,
    entry_email_staff,
    entry_date_emp,
    id_order_comp,
    id_pizza_comp,
    entry_id_order_comp,
    entry_id_pizza_comp,
    manager_cont,
    adress_cont,
    phonenumber_cont,
    email_cont,
    entry_manager_cont,
    entry_adress_cont,
    entry_phonenumber_cont,
    entry_email_cont,
    id_pizza_dp,
    description_dp,
    date_dp,
    entry_id_pizza_dp,
    entry_description_dp,
    entry_date_dp,
    pizza_name_menu,
    price_menu,
    coocking_time_menu,
    entry_pizza_name_menu,
    entry_price_menu,
    entry_coocking_time_menu,
    date_order_ord,
    id_staffer_ord,
    id_client_ord,
    entry_date_order_ord,
    entry_id_staffer_ord,
    entry_id_client_ord,
    id_pizza_rec,
    id_ingred_rec,
    entry_id_pizza_rec,
    entry_id_ingred_rec,
    id_stuffer_sch,
    weekday_sch,
    bwgwd_sch,
    endwd_sch,
    entry_id_stuffer_sch,
    entry_weekday_sch,
    entry_bwgwd_sch,
    entry_endwd_sch,
    name_ingred_wh,
    price_wh,
    delivery_date_wh,
    expiration_date_wh,
    entry_name_ingred_wh,
    entry_price_wh,
    entry_delivery_date_wh,
    entry_expiration_date_wh
                     ]
    for object_name in destroy_object:
        object_name.grid_forget()


# Функция для выбора вывода формы ввода
def BtnTableChoice():
    if role == 'Admin':
        DeleteAll()
        if combo_tables.get() == 'Clients':
            DeleteAll()
            ClientsGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Staff':
            DeleteAll()
            StaffGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Compositions':
            DeleteAll()
            CompositionsGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Contacts':
            DeleteAll()
            ContactsGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'DiscProm':
            DeleteAll()
            DiscPromGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Menu':
            DeleteAll()
            MenuGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Orders':
            DeleteAll()
            OrdersGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Recipes':
            DeleteAll()
            RecipesGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Schedule':
            DeleteAll()
            ScheduleGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Staff':
            DeleteAll()
            StaffGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)

        if combo_tables.get() == 'Warehouse':
            DeleteAll()
            WarehouseGrid()
            btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)


        if combo_tables.get() == 'client_exp':
            DeleteAll()
            btn_enter.grid_forget()

        if combo_tables.get() == 'inventory':
            DeleteAll()
            btn_enter.grid_forget()

        if combo_tables.get() == 'sales':
            DeleteAll()
            btn_enter.grid_forget()

        if combo_tables.get() == 'statistic':
            DeleteAll()
            btn_enter.grid_forget()

        if combo_tables.get() == 'summator':
            DeleteAll()
            btn_enter.grid_forget()

    TablesTables() # Обновляем таблицу

    #print('Таблица выбрана')
    #print(combo_tables.get())


# Выводим поля ввода для таблицы "Clients"
def ClientsGrid():
    name.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    sex.grid(row=1, column=1, stick='e', padx = 10, pady = 5)
    datebirth.grid(row=2, column=1, stick='e', padx = 10, pady = 5)
    phonenumber.grid(row=3, column=1, stick='e', padx = 10, pady = 5)
    email.grid(row=4, column=1, stick='e', padx = 10, pady = 5)

    entry_name.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_sex.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)
    entry_datebirth.grid(row=2, column=2, stick='ew', padx = 10, pady = 5)
    entry_phonenumber.grid(row=3, column=2, stick='ew', padx = 10, pady = 5)
    entry_email.grid(row=4, column=2, stick='ew', padx = 10, pady = 5)

# Выводим поля ввода для таблицы "Staff"
def StaffGrid():
    name_staff.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    sex_staff.grid(row=1, column=1, stick='e', padx = 10, pady = 5)
    post.grid(row=2, column=1, stick='e', padx = 10, pady = 5)
    salary.grid(row=3, column=1, stick='e', padx = 10, pady = 5)
    passport_series.grid(row=4, column=1, stick='e', padx = 10, pady = 5)
    passport_number.grid(row=5, column=1, stick='e', padx = 10, pady = 5)
    datebirth_staff.grid(row=6, column=1, stick='e', padx = 10, pady = 5)
    phonenumber.grid(row=7, column=1, stick='e', padx = 10, pady = 5)
    email_staff.grid(row=8, column=1, stick='e', padx = 10, pady = 5)
    date_emp.grid(row=9, column=1, stick='e', padx = 10, pady = 5)

    entry_name_staff.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_sex_staff.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)
    entry_post.grid(row=2, column=2, stick='ew', padx = 10, pady = 5)
    entry_salary.grid(row=3, column=2, stick='ew', padx = 10, pady = 5)
    entry_passport_series.grid(row=4, column=2, stick='ew', padx = 10, pady = 5)
    entry_passport_number.grid(row=5, column=2, stick='ew', padx = 10, pady = 5)
    entry_datebirth_staff.grid(row=6, column=2, stick='ew', padx = 10, pady = 5)
    entry_phonenumber.grid(row=7, column=2, stick='ew', padx = 10, pady = 5)
    entry_email_staff.grid(row=8, column=2, stick='ew', padx = 10, pady = 5)
    entry_date_emp.grid(row=9, column=2, stick='ew', padx = 10, pady = 5)

# Выводим поля ввода для таблицы "Warehouse"
def WarehouseGrid():
    name_ingred_wh.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    price_wh.grid(row=1, column=1, stick='e', padx = 10, pady = 5)
    delivery_date_wh.grid(row=2, column=1, stick='e', padx = 10, pady = 5)
    expiration_date_wh.grid(row=3, column=1, stick='e', padx = 10, pady = 5)

    entry_name_ingred_wh.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_price_wh.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)
    entry_delivery_date_wh.grid(row=2, column=2, stick='ew', padx = 10, pady = 5)
    entry_expiration_date_wh.grid(row=3, column=2, stick='ew', padx = 10, pady = 5)


# Выводим поля ввода для таблицы "Orders"
def OrdersGrid():
    date_order_ord.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    id_staffer_ord.grid(row=1, column=1, stick='e', padx = 10, pady = 5)
    id_client_ord.grid(row=2, column=1, stick='e', padx = 10, pady = 5)

    entry_date_order_ord.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_id_staffer_ord.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)
    entry_id_client_ord.grid(row=2, column=2, stick='ew', padx = 10, pady = 5)

# Выводим поля ввода для таблицы "Contacts"
def ContactsGrid():
    manager_cont.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    adress_cont.grid(row=1, column=1, stick='e', padx = 10, pady = 5)
    phonenumber_cont.grid(row=2, column=1, stick='e', padx = 10, pady = 5)
    email_cont.grid(row=3, column=1, stick='e', padx = 10, pady = 5)

    entry_manager_cont.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_adress_cont.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)
    entry_phonenumber_cont.grid(row=2, column=2, stick='ew', padx = 10, pady = 5)
    entry_email_cont.grid(row=3, column=2, stick='ew', padx = 10, pady = 5)


# Выводим поля ввода для таблицы "Recipes"
def RecipesGrid():
    id_pizza_rec.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    id_ingred_rec.grid(row=1, column=1, stick='e', padx = 10, pady = 5)

    entry_id_pizza_rec.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_id_ingred_rec.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)

# Выводим поля ввода для таблицы "Compositions"
def CompositionsGrid():
    id_order_comp.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    id_pizza_comp.grid(row=1, column=1, stick='e', padx = 10, pady = 5)

    entry_id_order_comp.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_id_pizza_comp.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)

# Выводим поля ввода для таблицы "Menu"
def MenuGrid():
    pizza_name_menu.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    price_menu.grid(row=1, column=1, stick='e', padx = 10, pady = 5)
    coocking_time_menu.grid(row=2, column=1, stick='e', padx = 10, pady = 5)

    entry_pizza_name_menu.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_price_menu.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)
    entry_coocking_time_menu.grid(row=2, column=2, stick='ew', padx = 10, pady = 5)

# Выводим поля ввода для таблицы "DiscProm"
def DiscPromGrid():
    id_pizza_dp.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    description_dp.grid(row=1, column=1, stick='e', padx = 10, pady = 5)
    date_dp.grid(row=2, column=1, stick='e', padx = 10, pady = 5)

    entry_id_pizza_dp.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_description_dp.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)
    entry_date_dp.grid(row=2, column=2, stick='ew', padx = 10, pady = 5)


# Выводим поля ввода для таблицы "Schedule"
def ScheduleGrid():
    id_stuffer_sch.grid(row=0, column=1, stick='e', padx = 10, pady = 5)
    weekday_sch.grid(row=1, column=1, stick='e', padx = 10, pady = 5)
    bwgwd_sch.grid(row=2, column=1, stick='e', padx = 10, pady = 5)
    endwd_sch.grid(row=3, column=1, stick='e', padx = 10, pady = 5)

    entry_id_stuffer_sch.grid(row=0, column=2, stick='ew', padx = 10, pady = 5)
    entry_weekday_sch.grid(row=1, column=2, stick='ew', padx = 10, pady = 5)
    entry_bwgwd_sch.grid(row=2, column=2, stick='ew', padx = 10, pady = 5)
    entry_endwd_sch.grid(row=3, column=2, stick='ew', padx = 10, pady = 5)


# Функция вывода таблицы
def TablesTables():
    if combo_tables.get() == 'Clients':
        lst = GetData_Clients()
        heads = ['ID', 'Имя', 'пол', 'дата рождения', 'телефон', 'почта']

    if combo_tables.get() == 'Staff':
        lst = GetData_Staff()
        heads = ['ID', 'Имя', 'пол', 'должность', 'зарплата', 'серия паспорта', 'номер паспорта', 'дата рождения', 'телефон', 'почта', 'дата приема на работу']

    if combo_tables.get() ==  'Compositions':
        lst = GetData_Compositions()
        heads = ['ID состава', 'ID заказа', 'ID пиццы' ]

    if combo_tables.get() == 'Contacts':
        lst = GetData_Contacts()
        heads = ['ID', 'контактное лицо', 'адресс', 'номер телефона', 'эл.почта',]

    if combo_tables.get() ==  'DiscProm':
        lst = GetData_DiscProm()
        heads = ['ID', 'пицца', 'описание', 'дата проведения']

    if combo_tables.get() ==  'Menu':
        lst = GetData_Menu()
        heads = ['ID', 'пицца', 'цена', 'время приготовления']

    if combo_tables.get() == 'Orders':
        lst = GetData_Orders()
        heads = ['ID', 'дата', 'сотрудник', 'клиент']

    if combo_tables.get() == 'Recipes':
        lst = GetData_Recipes()
        heads = ['ID', 'пицца', 'ингридиент']

    if combo_tables.get() == 'Schedule':
        lst = GetData_Schedule()
        heads = ['ID', 'работник', 'день недели', 'начало рабочего дня',  'конец рабочего дня']

    if combo_tables.get() == 'Warehouse':
        lst = GetData_Warehouse()
        heads = ['ID', 'ингридиент', 'цена', 'дата поставки', 'срок годности']

    if combo_tables.get() == 'client_exp':
        lst = GetData_client_exp()
        heads = ['клиент', 'заказ', 'пицца', 'цена']

    if combo_tables.get() == 'inventory':
        lst = GetData_inventory()
        heads = ['ингридиент', 'кол-во']

    if combo_tables.get() == 'sales':
        lst = GetData_sales()
        heads = ['пицца', 'продажи']

    if combo_tables.get() == 'statistic':
        lst = GetData_statistic()
        heads = ['дата', 'количество заказов']

    if combo_tables.get() == 'summator':
        lst = GetData_summator()
        heads = ['заказ', 'сумма']

    tabl = ttk.Treeview(win, show='headings')
    tabl['columns'] = heads
    #tabl['displaycolumns'] = [пишешь здесь свой порядок столбцов]
    for header in heads:
        tabl.heading(header, text=header, anchor='center')
        tabl.column(header, anchor='center', width=135)
    for row in lst:
        tabl.insert('', END, values=row)


    scroll_pane = ttk.Scrollbar(win, orient=VERTICAL, command=tabl.yview)
    tabl.configure(yscrollcommand=scroll_pane.set)

    scroll_pane.grid(column=3, row=11, rowspan=5,  sticky=(N, S))
    tabl.grid(row=11, column=0, columnspan=3, sticky='ew', padx=10, pady=10)


# Блок кода, отвечающий за предварительное создание всех виджетов и интерфейса
# Список всех таблиц и представлений
#tables = ['Clients', 'Compositions', 'Contacts', 'DiscProm', 'Menu', 'Orders', 'Recipes', 'Schedule',
    #      'Staff', 'Warehouse', 'client_exp', 'inventory', 'sales', 'statistic', 'summator']

def RoleT(role):
    if role == 'Admin':
        t = ['Clients', 'Compositions', 'Contacts', 'DiscProm', 'Menu', 'Orders', 'Recipes', 'Schedule',
                  'Staff', 'Warehouse', 'client_exp', 'inventory', 'sales', 'statistic', 'summator']

    if role == 'Waiter':
        t = ['Clients', 'Compositions', 'DiscProm', 'Menu', 'Orders', 'Schedule']

    if role == 'Cook':
        t = ['Compositions', 'Menu', 'Orders', 'Recipes', 'Schedule', 'Warehouse']

    if role == 'Guest':
        t = ['DiscProm', 'Menu', 'Contacts']
    return(t)



# Комбобокс для выбора таблицы
combo_tables = ttk.Combobox(win, values = RoleT(role))
combo_tables.current(0)
btn_table_choice = Button(win, text = 'выбрать', command = BtnTableChoice)
# Вывод комбобокса
combo_tables.grid(row=0, column=0, stick='ew', padx = 10, pady = 10)
btn_table_choice.grid(row=1, column=0, stick='ew', padx = 10, pady = 10)
#Кнопка для ввода информации в базу"Ввести"
if role == 'Admin':
    btn_enter = Button(win, text = 'Ввести', command = BtnEnter)
    btn_enter.grid(row=10, column=2, stick='ew', padx = 10, pady = 10)


#Создаем таблицу
TablesTables()


# Задаем ширину колон
win.grid_columnconfigure(0, minsize = 100)                                      # Настройка величины полей/столбцов
win.grid_columnconfigure(1, minsize = 10)
win.grid_columnconfigure(2, minsize = 200)


#Clients
name = Label(win, text='имя клиента')
sex = Label(win, text='пол')
datebirth = Label(win, text='дата рождения')
phonenumber = Label(win, text='номер телефона')
email = Label(win, text='эл.почта')

entry_name = Entry(win)
entry_sex = Entry(win)
entry_datebirth = DateEntry(win)
entry_phonenumber = Entry(win)
entry_email = Entry(win)


#Staff
name_staff = Label(win, text='имя сотрудника')
sex_staff = Label(win, text='пол')
post = Label(win, text='должность')
salary = Label(win, text='зарплата')
passport_series = Label(win, text='серия паспорта')
passport_number = Label(win, text='номер пааспорта')
datebirth_staff = Label(win, text='дата рождения')
phonenumber = Label(win, text='номе ртелефона')
email_staff = Label(win, text='эл.почта')
date_emp = Label(win, text='дата приема на работу')

entry_name_staff = Entry(win)
entry_sex_staff = Entry(win)
entry_post = Entry(win)
entry_salary = Entry(win)
entry_passport_series = Entry(win)
entry_passport_number = Entry(win)
entry_datebirth_staff = DateEntry(win)
entry_phonenumber = Entry(win)
entry_email_staff = Entry(win)
entry_date_emp = DateEntry(win)


# Compositions
id_order_comp = Label(win, text='Заказ')
id_pizza_comp = Label(win, text='Пицца')

entry_id_order_comp = Entry(win)
entry_id_pizza_comp = Entry(win)


# Contacts
manager_cont = Label(win, text='Контактное лицо')
adress_cont = Label(win, text='адресс')
phonenumber_cont = Label(win, text='номе телефона')
email_cont = Label(win, text='эл.почта')

entry_manager_cont = Entry(win)
entry_adress_cont = Entry(win)
entry_phonenumber_cont = Entry(win)
entry_email_cont = Entry(win)


# DiscProm
id_pizza_dp = Label(win, text='пицца')
description_dp = Label(win, text='описание')
date_dp = Label(win, text='крайняя дата предложения')

entry_id_pizza_dp = Entry(win)
entry_description_dp = Entry(win)
entry_date_dp = DateEntry(win)


# Menu
pizza_name_menu = Label(win, text='пицца')
price_menu = Label(win, text='цена')
coocking_time_menu = Label(win, text=' время приготовления')

entry_pizza_name_menu = Entry(win)
entry_price_menu = Entry(win)
entry_coocking_time_menu = Entry(win)


# Orders
date_order_ord = Label(win, text='дата заказа')
id_staffer_ord = Label(win, text='работник')
id_client_ord = Label(win, text='клиент')

entry_date_order_ord = DateEntry(win)
entry_id_staffer_ord = Entry(win)
entry_id_client_ord = Entry(win)


# Recipes
id_pizza_rec = Label(win, text='пицца')
id_ingred_rec = Label(win, text='ингридиент')

entry_id_pizza_rec = Entry(win)
entry_id_ingred_rec = Entry(win)


# Schedule
id_stuffer_sch = Label(win, text='работник')
weekday_sch = Label(win, text='день недели')
bwgwd_sch = Label(win, text='начало рабочего дня')
endwd_sch = Label(win, text='конец рабочего дня')

entry_id_stuffer_sch = Entry(win)

weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
entry_weekday_sch = ttk.Combobox(win, values = weekdays)
entry_bwgwd_sch = Entry(win)
entry_endwd_sch = Entry(win)


# Warehouse
name_ingred_wh = Label(win, text='ингридиент')
price_wh = Label(win, text='цена')
delivery_date_wh = Label(win, text='дата поставки')
expiration_date_wh = Label(win, text='срок годности')

entry_name_ingred_wh = Entry(win)
entry_price_wh = Entry(win)
entry_delivery_date_wh = DateEntry(win)
entry_expiration_date_wh = DateEntry(win)



win.mainloop()
