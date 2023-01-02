import PySimpleGUI as pg 
import sql
#def that creates a new window of list of sheeps
def update_delete(selected_row,cur):
	sheep_layout = [[pg.Text('id', size=(15, 1)), pg.InputText(selected_row[0], key='-id-')],
					[pg.Text('age', size=(15, 1)), pg.InputText(selected_row[1], key='-age-')],
					[pg.Text('farm', size=(15, 1)), pg.InputText(selected_row[2], key='-farm-')],
					[pg.Text('category', size=(15, 1)), pg.InputText(selected_row[3], key='-category-')],
					[pg.Button("update")], [pg.Button("delete"),pg.Button("cancel")]]
	window_ud = pg.Window("sheep", sheep_layout)
	while True:
		event_ud, values_ud = window_ud.read()
		if event_ud == "cancel" or event_ud == pg.WIN_CLOSED:
			break
		elif event_ud == "delete":
			cur.execute(sql.delete_sheep,(str(values_ud['-id-']),))
			window_ud.close()
			break
		elif event_ud == "update":
			cur.execute(sql.update_sheep, (str(values_ud['-age-']),str(values_ud['-farm-']),str(values_ud['-category-']),str(values_ud['-id-'])))
			window_ud.close()
			break
def show_table(sheeps_informations_array,cur):
	heading=['id', 'age', 'farm','category']
	sheeps_information_window_layout =[[pg.Table(values=sheeps_informations_array,headings=heading,max_col_width=50,display_row_numbers=True,enable_events=True,key='-SHEEPS_TABLE-',)]]
	sheeps_information_window = pg.Window("sheeps Window",
	sheeps_information_window_layout, modal=True)

	while True:
		event, values = sheeps_information_window.read()
		if event == "Exit" or event == pg.WIN_CLOSED:
			break
		if (event == '-SHEEPS_TABLE-'):
			selected_index = values['-SHEEPS_TABLE-'][0]
			selected_row = sheeps_informations_array[selected_index]
			update_delete(selected_row,cur)
		sheeps_information_window.close()
