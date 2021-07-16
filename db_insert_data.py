import mysql.connector




conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    port =3306,
    password="NEWPASSWORD",
    auth_plugin='mysql_native_password'
)

#Descomente se quiser desfazer o banco
# conexao.cursor().execute("DROP DATABASE 'Troubleshooting';")
# conexao.commit()


cursor = conexao.cursor()


# inserindo usuarios

cursor.executemany(
    'INSERT INTO troubleshooting.users (id_user, name, pwd) VALUES (%s, %s, %s)',
    [
        ('luan', 'Luan Marques', 'flask'),
        ('nico', 'Nico', '7a1'),
        ('danilo', 'Danilo', 'vegas'),
        ('luiz', 'Luiz Fernando', '1234')
    ])


# inserindo fault
cursor.executemany(
    'INSERT INTO troubleshooting.fault (description_fault) VALUES (%s,)',
    [
        ('Module (head) is not detected on the HMI panel'),
        ('Ready to rearm status does not appear'),

    ])
# inserindo cause
cursor.executemany(
    'INSERT INTO troubleshooting.cause (description_cause) VALUES (%s,)',
    [
        ('Incorrect connections of the head'),
        ('Engaged emergency stop or active alarm'),

    ])
# inserindo resolution_method
cursor.executemany(
    'INSERT INTO troubleshooting.resolution (description_resolution) VALUES (%s,)',
    [
        'Check the head connection',
        'Check if all the emergency stops are disengaged and reset the alarms',

    ])
# inserindo reference
cursor.executemany(
    'INSERT INTO troubleshooting.reference (description_reference) VALUES (%s,)',
    [
        ('Figure 3.9'),
        ('Section 3.5'),

    ])

cursor.executemany(
    "INSERT INTO troubleshooting.trouble_relation (description_fault, description_cause, description_resolution, "
    "description_reference) VALUES (%s, %s, %s, %s)",
    [
        ('Module (head) is not detected on the HMI panel', 'Incorrect connections of the head', 'Check the head connection', 'Figure 3.9'),
        ('Ready to rearm status does not appear', 'Engaged emergency stop or active alarm', 'Check if all the emergency stops are disengaged and reset the alarms', 'Section 3.5'),

    ])
cursor.execute('select * from troubleshooting.fault')
print(' -------------  fault:  -------------')
for fault in cursor.fetchall():
    print(fault[1])

cursor.execute('select * from troubleshooting.cause')
print(' -------------  cause:  -------------')
for cause in cursor.fetchall():
    print(cause[1])

cursor.execute('select * from troubleshooting.resolution_method')
print(' -------------  resolution:  -------------')
for resolution in cursor.fetchall():
    print(resolution[1])

cursor.execute('select * from troubleshooting.reference')
print(' -------------  reference:  -------------')
for reference in cursor.fetchall():
    print(reference[1])

cursor.execute('select * from troubleshooting.trouble_relation')
print(' -------------  trouble:  -------------')
for trouble in cursor.fetchall():
    print(trouble[1])

cursor.execute('select * from troubleshooting.user')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])


# commitando senão nada tem efeito
conexao.commit()