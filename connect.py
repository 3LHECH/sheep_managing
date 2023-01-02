import PySimpleGUI as pg
import layouts as l
import sql
import re
import os
from dotenv import load_dotenv
def check_input(values):
    #this function is for cheking if the user is inputing right things
    var = 1 #if var is one then there is no problem if a#1 then there is a msitake in the input
    if (values['phone_number'].isdigit() and len(list(values['phone_number']))!=8)==True and re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', values["email"], re.I)==None :
        var =4
    elif(values['phone_number'].isdigit() and len(list(values['phone_number']))!=8)==True:
        var = 3
    elif re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', values["email"], re.I)==None:
        var = 2
    return var
def input_validation (value_create_user,window_create_user):
    var = 1
    if check_input(value_create_user) == 4:
        window_create_user['_email_warn_'].Update(visible=True)
        window_create_user['_phone_number_warn_'].Update(visible=True)
        var=0
    elif check_input(value_create_user) == 3:
        window_create_user['_phone_number_warn_'].Update(visible=True)
        var = 0
    elif check_input(value_create_user) == 2:
        window_create_user['_email_warn_'].Update(visible=True)
        var = 0
    return var
def create_account(cur):
    # a function to create an account
    admin=False
    main_layouts_create_user = [
        [pg.Text("enter first_name"), pg.InputText(key='first_name', do_not_clear=False)],
        [pg.Text("enter family_name"), pg.InputText(key='family_name', do_not_clear=False)],
        [pg.Text("enter email"), pg.InputText(key='email', do_not_clear=False)],
        [pg.Text("email is not valid", key='_email_warn_', visible=False)],
        [pg.Text("enter phone_number"), pg.InputText(key='phone_number', do_not_clear=False)],
        [pg.Text("phone number is not valid", key='_phone_number_warn_', visible=False)],
        [pg.Text("enter password"), pg.InputText(key='password', do_not_clear=False)],
        [pg.Text("etner dbpwd"), pg.InputText(key='dbpwd', do_not_clear=False)],
        [pg.Button("create user"), pg.Button("Cancel")]
    ]
    window_create_user = pg.Window("Create_user", main_layouts_create_user)
    while_true=1
    while while_true==1:
        event_create_user, value_create_user = window_create_user.read()
        if event_create_user=="Cancel" or event_create_user == pg.WIN_CLOSED:
            window_create_user.close()
            return 0
        elif event_create_user == "create user":
            if(input_validation(value_create_user,window_create_user)==1):
                load_dotenv()
                if(value_create_user['dbpwd']==os.environ.get('DB_PWD')):
                    admin=True
                cur.execute(sql.create_users)
                values = (value_create_user['first_name'], value_create_user['family_name'], value_create_user['email'],
                          value_create_user['phone_number'],value_create_user['password'][::-1],str(admin))
                cur.execute(sql.insert_script_users, values)
                window_create_user.close()
                return 0
            else:
                window_create_user.close()
                return 0
        while_true==0

def check_user(value,cur):
    cur.execute(sql.show_users)
    results = cur.fetchall()
    for row in results:
        if value['first_name']==row[0] and value['password']==row[4]:
            return 1
    return 0