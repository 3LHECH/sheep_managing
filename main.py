import PySimpleGUI as pg
import python_to_postgres
import connect
import psycopg2.extras
import os
from dotenv import load_dotenv
load_dotenv()
hostname = 'localhost'
databasename = os.environ.get('DB_USER')
username = os.environ.get('DB_USERNAME')
pwd = os.environ.get('DB_PWD')
port_id = 5432
conn = None

main_layout=[
    [pg.Text("enter first_name"),pg.InputText(key='first_name',do_not_clear=False)],
    [pg.Text("enter password"),pg.InputText(key='password',do_not_clear=False)],
    [pg.Button("Connect"),pg.Button("Create account")]
]

window = pg.Window("krib",main_layout)

try:
    with psycopg2.connect(
            host='localhost',
            dbname=os.environ.get('DB_USER'),
            user=os.environ.get('DB_USERNAME'),
            password=os.environ.get('DB_PWD'),
            port=5432) as conn:
        cur = conn.cursor()
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            while True:
                event , value = window.read()
                if event == "Connect" :
                    if connect.check_user(value,cur)==1:
                        window.close()
                        python_to_postgres.entering(cur)
                    else:
                        pg.Popup("this user doesn't exist \n wrong password or maybe username")
                elif event=="Create account":
                    connect.create_account(cur)

                else :
                    break
except Exception as error:
    print(error)
finally:
    if conn is not None:
        cur.close()
        conn.close()
