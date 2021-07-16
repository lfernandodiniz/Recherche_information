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

cursor.execute('create database if not exists Troubleshooting')
cursor.execute('use Troubleshooting')
cursor.execute("""create table if not exists fault(
                 description_fault varchar(500) primary key collate utf8_bin  not null,                 
                 )"""
                )
cursor.execute("""create table if not exists cause(
                 description_cause varchar(500) primary key collate utf8_bin  not null,                
                 )"""
                )
cursor.execute("""create table if not exists resolution_method(
                 description_resolution varchar(500) primary key collate utf8_bin  not null,                
                 )"""
                )
cursor.execute("""create table if not exists reference(
                 description_reference varchar(500) primary key collate utf8_bin  not null,              
                 )"""
                )
cursor.execute("""create table if not exists trouble_relation(
                 id_trouble int(11) not null auto_increment,
                 description_fault varchar(500) collate utf8_bin not null,
                 description_cause varchar(500) collate utf8_bin not null,
                 description_resolution varchar(500) collate utf8_bin not null,
                 description_reference varchar(500) collate utf8_bin not null,
                 primary key (id_trouble),
                 key description_fault (description_fault), key description_cause (description_cause),
                 key description_resolution (description_resolution), key description_reference (description_reference),
                 CONSTRAINT trouble_relation_ibfk_1 foreign key (description_fault),                
                 REFERENCES fault (description_fault) ON DELETE CASCADE,
                 CONSTRAINT `trouble_relation_ibfk_2` foreign key (description_cause),
                 REFERENCES cause (description_cause) ON DELETE CASCADE,
                 CONSTRAINT trouble_relation_ibfk_3 foreign key (description_resolution),
                 REFERENCES resolution (description_resolution) ON DELETE CASCADE,
                 CONSTRAINT trouble_relation_ibfk_4 foreign key (description_reference),
                 REFERENCES reference (description_reference) ON DELETE CASCADE,
                 )engine=innodb default charset=utf8 collate=utf8_bin"""
                )



cursor.execute("""create table if not exists usuario (
                id varchar(8) PRIMARY KEY not null,
                nome varchar(20) not null,
                senha varchar(8) not null
                )"""
               )
# inserindo usuarios

cursor.executemany(
    'INSERT INTO Troubleshooting.usuario (id, nome, senha) VALUES (%s, %s, %s)',
    [
        ('luan', 'Luan Marques', 'flask'),
        ('nico', 'Nico', '7a1'),
        ('danilo', 'Danilo', 'vegas'),
        ('luiz', 'Luiz Fernando', '2385')
    ])

cursor.execute('select * from Troubleshooting.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo fault
cursor.executemany(
    'INSERT INTO Troubleshooting.fault (description_fault) VALUES (%s,)',
    [
        ('Module (head) is not detected on the HMI panel'),
        ('Ready to rearm status does not appear'),

    ])
# inserindo cause
cursor.executemany(
    'INSERT INTO Troubleshooting.cause (description_cause) VALUES (%s,)',
    [
        ('Incorrect connections of the head'),
        ('Engaged emergency stop or active alarm'),

    ])
# inserindo resolution_method
cursor.executemany(
    'INSERT INTO Troubleshooting.resolution (description_resolution) VALUES (%s,)',
    [
        'Check the head connection',
        'Check if all the emergency stops are disengaged and reset the alarms',

    ])
# inserindo reference
cursor.executemany(
    'INSERT INTO Troubleshooting.reference (description_reference) VALUES (%s,)',
    [
        'Figure 3.9',
        ('Section 3.5'),

    ])

cursor.executemany(
    "INSERT INTO Troubleshooting.trouble_relation (description_fault, description_cause, description_resolution, "
    "description_reference) VALUES (%s, %s, %s, %s)",
    [
        ('Module (head) is not detected on the HMI panel', 'Incorrect connections of the head', 'Check the head connection', 'Figure 3.9'),
        ('Ready to rearm status does not appear', 'Engaged emergency stop or active alarm', 'Check if all the emergency stops are disengaged and reset the alarms', 'Section 3.5'),

    ])
cursor.execute('select * from Troubleshooting.fault')
print(' -------------  fault:  -------------')
for fault in cursor.fetchall():
    print(fault[1])

cursor.execute('select * from Troubleshooting.cause')
print(' -------------  cause:  -------------')
for cause in cursor.fetchall():
    print(cause[1])

cursor.execute('select * from Troubleshooting.resolution')
print(' -------------  resolution:  -------------')
for resolution in cursor.fetchall():
    print(resolution[1])

cursor.execute('select * from Troubleshooting.reference')
print(' -------------  reference:  -------------')
for reference in cursor.fetchall():
    print(reference[1])

cursor.execute('select * from Troubleshooting.trouble')
print(' -------------  trouble:  -------------')
for trouble in cursor.fetchall():
    print(trouble[1])
# commitando senão nada tem efeito
conexao.commit()
conexao.close()