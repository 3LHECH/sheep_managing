import psycopg2
import psycopg2.extras
import PySimpleGUI as pg 
import list_of_sheeps 
import sql
def entering(cur):

	python_to_postegres_layout = [
		[
			pg.Text("enter number :", size=(10, 2)), pg.InputText(key='id', do_not_clear=False)
		],
		[
			pg.Text("enter age:", size=(10, 2)), pg.InputText(key='age', do_not_clear=False)
		],
		[
			pg.Text("farm:", size=(10, 2)), pg.InputText(key='farm', do_not_clear=False)
		],
		[
			pg.Text("choose sex"),
			pg.Radio("Male", "group1"),
			pg.Radio("Female", "group1")
		],
		[
			pg.Button("ok"), pg.Button("show table"), pg.Button("Cancel"), pg.Button("new")
		],

	]

	window = pg.Window("krib", python_to_postegres_layout)
	cur.execute(sql.create_script)
	while True:
		event , value = window.read()
		if event == "Cancel" or event == pg.WIN_CLOSED:
			break
		elif event == "ok":
			sex = "Female"
			if value[0] == True:
				sex = "Male"
			values = (value["id"], value["age"], value["farm"], sex)
			cur.execute(sql.insert_script_sheeps, values)
		elif event == 'show table' :
			cur.execute(sql.show_table)
			list_of_sheeps.show_table(cur.fetchall(),cur)
