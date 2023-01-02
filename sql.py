'''this file contain all sql for my project'''
create_users = '''CREATE TABLE IF NOT EXISTS worker(
                                    first_name    varchar(25),
                                    family_name     varchar(25),
                                    email         varchar(25),
                                    phone_number    int ,
                                    password        varchar(25),
                                    admin           BOOLEAN);'''
create_script = ''' CREATE TABLE IF NOT EXISTS sheeps(
										id      int PRIMARY KEY,
										age     int NOT NULL,
										farm	varchar(40),
										category    varchar(40) NOT NULL); '''
insert_script_sheeps = 'INSERT INTO sheeps (id, age, farm, category) VALUES (%s, %s, %s, %s)'
insert_script_users = 'INSERT INTO worker (first_name, family_name, email,phone_number,password,admin ) VALUES (%s, %s, %s, %s,%s,%s)'
show_table='SELECT * FROM sheeps ORDER BY id'
show_users = 'SELECT * FROM worker '
delete_sheep='DELETE FROM sheeps WHERE id=%s '
update_sheep='UPDATE sheeps SET age = %s,farm = %s,category = %s WHERE id=%s '
