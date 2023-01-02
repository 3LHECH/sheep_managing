import PySimpleGUI as pg
main_layout=[
    [pg.Text("enter first_name"),pg.InputText(key='first_name',do_not_clear=False)],
    [pg.Text("enter password"),pg.InputText(key='password',do_not_clear=False)],
    [pg.Button("Connect"),pg.Button("Create account")]
]
main_layouts_create_user=[
	[pg.Text("enter first_name"),pg.InputText(key='first_name',do_not_clear=False)],
	[pg.Text("enter family_name"),pg.InputText(key='family_name',do_not_clear=False)],
	[pg.Text("enter email"),pg.InputText(key='email',do_not_clear=False)],
	[pg.Text("email is not valid",key='_email_warn_',visible=False)],
	[pg.Text("enter phone_number"),pg.InputText(key='phone_number',do_not_clear=False)],
	[pg.Text("phone number is not valid",key='_phone_number_warn_',visible=False)],
	[pg.Text("enter password"),pg.InputText(key='password',do_not_clear=False)],
	[pg.Text("etner dbpwd"), pg.InputText(key='dbpwd', do_not_clear=False)],
	[pg.Button("create user"),pg.Button("Cancel")]
]

python_to_postegres_layout=[
		[
		pg.Text("enter number :",size=(10,2)),pg.InputText(key='id',do_not_clear=False)
		],
		[
		pg.Text("enter age:",size=(10,2)),pg.InputText(key='age',do_not_clear=False)
		],
		[
		pg.Text("farm:",size=(10,2)),pg.InputText(key='farm',do_not_clear=False)
		],
		[
		pg.Text("choose sex"),
		pg.Radio("Male","group1"),
		pg.Radio("Female","group1")
		],
		[
			pg.Button("ok"),pg.Button("show table"),pg.Button("Cancel"),pg.Button("new")
		],

	]

