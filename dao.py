from models import User, Trouble_relation
import mysql.connector

cnx = mysql.connector.connect(host="localhost",
                              user="root",
                              port=3306,
                              password="NEWPASSWORD",
                              auth_plugin='mysql_native_password', database='troubleshooting')
cursor = cnx.cursor()

# DAO = Data access object
SQL_DELETE_TROUBLE = 'delete from trouble_relation where trouble_no = %s'
SQL_DELETE_fault_no = 'delete from %s where fault_no = %s'
SQL_TROUBLE_POR_ID = 'SELECT trouble_no, description_fault, description_cause, ' \
                     'description_resolution, description_reference FROM trouble_relation where trouble_no = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_TROUBLE = 'UPDATE jogo SET nome=%s, categoria=%s, console=%s where id = %s'
SQL_BUSCA_TROUBLE = 'SELECT trouble_no, description_fault, description_cause, ' \
                    'description_resolution, description_reference FROM trouble_relation'
SQL_CRIA_TROUBLE = 'INSERT into jogo (nome, categoria, console) values (%s, %s, %s)'

SQL_CHECK_VALUE = ("SELECT IF (COUNT(*) > 0, 'exist', 'not_exist') FROM %(table)s WHERE %(column)s = %(value)s")



class TroubleDao:
    def __init__(self, db):
        self.__db = db


    def salvar(self, trouble):
        # cursor = self.__db.cursor()
        # print(trouble.trouble_no)
        # if (trouble.trouble_no):
        #
        #     print("updating table...")
        #
        #     update_fault = ("UPDATE fault SET "
        #                     "description_fault = %s "
        #                     "WHERE trouble_no = %s"
        #                     )
        #
        #     update_cause = ("UPDATE cause SET "
        #                     "description_cause = %s "
        #                     "WHERE trouble_no = %s")
        #
        #     update_resolution = ("UPDATE resolution_method SET "
        #                         "description_resolution = %s "
        #                         "WHERE trouble_no = %s"
        #                          )
        #
        #     update_reference = ("UPDATE reference SET "
        #                         "description_reference = %s "
        #                         "WHERE trouble_no = %s")
        #
        #     update_trouble_relation = ("UPDATE trouble_relation SET "
        #                                "description_fault = %(description_fault)s, "
        #                                "description_cause = %(description_cause)s, "
        #                                "description_resolution = %(description_resolution)s, "
        #                                "description_reference = %(description_reference)s "
        #                                "WHERE trouble_no = %(fault_no)s")
        #
        #
        #
        #
        #     # alter_fault
        #     data_fault = (trouble.description_fault, trouble.fault_no)
        #     cursor.execute(update_fault, data_fault)
        #     print("inside edit", trouble.fault_no)
        #
        #     # alter_cause
        #     data_cause = (trouble.description_cause, trouble.fault_no)
        #     cursor.execute(update_cause, data_cause)
        #
        #     # alter resolution_method
        #     data_resolution = (trouble.description_resolution, trouble.fault_no)
        #
        #     cursor.execute(update_resolution, data_resolution)
        #
        #     # alter reference
        #     data_reference = (trouble.description_reference, trouble.fault_no)
        #     cursor.execute(update_reference, data_reference)
        #
        #     # alter trouble_relation
        #     # data_trouble_relation = {
        #     #     'description_fault': trouble.description_fault,
        #     #     'description_cause': trouble.description_cause,
        #     #     'description_resolution': trouble.description_resolution,
        #     #     'description_reference': trouble.description_reference,
        #     #
        #     # }
        #     # cursor.execute(update_trouble_relation, data_trouble_relation)
        #
        #
        #
        #     cnx.commit()
        #     # cursor.close()
        #     # cnx.close()
        #     return trouble


        # else:
            #trouble = insert_data(trouble)
            #cursor.execute(SQL_CRIA_JOGO, (jogo.nome, jogo.categoria, jogo.console))
            #jogo.id = cursor.lastrowid
            #self.__db.commit()

            # add's

            # print(f"fault: {trouble.description_fault}, cause: {trouble.description_cause}, resolution: {trouble.description_resolution},"
            #       f" reference: {trouble.description_reference}, trouble_no: {trouble.trouble_no}, fault_no: {trouble.fault_no}")


        add_fault = ("INSERT INTO fault "
                    "(description_fault) "
                    "VALUES ( %(description_fault)s)")

        add_cause = ("INSERT INTO cause "
                    "(description_cause) "
                    "VALUES (%(description_cause)s)")

        add_resolution = ("INSERT INTO resolution_method "
                         "(description_resolution) "
                         "VALUES (%(description_resolution)s)")

        add_reference = ("INSERT INTO reference "
                        "(description_reference) "
                        "VALUES (%(description_reference)s)")

        add_trouble_relation = ("INSERT INTO trouble_relation "
                               "(description_fault, description_cause, description_resolution, description_reference) "
                               "VALUES ( %(description_fault)s, %(description_cause)s, %(description_resolution)s, %(description_reference)s)")



        # ("UPDATE reference SET "
        #         #  "description_reference = %s "
        #         #  "WHERE trouble_no = %s")

        # insert_fault

        table = 'fault'
        colunm = 'description_fault'
        data_analyze = {
          'value': trouble.description_fault,
                        }
        cursor.execute(f"SELECT IF (COUNT(*) > 0, 'exist', 'not_exist') FROM {table} WHERE {colunm} = %(value)s", data_analyze)
        data = cursor.fetchall()
        exist = [str(x) for x, in data]

        if (exist[0] == 'not_exist'):
            data_fault = {
               'description_fault': trouble.description_fault,
            }
            cursor.execute(add_fault, data_fault)
            #trouble.fault_no = cursor.lastrowid

        # insert_cause

        # check before if there is the value, if not, add a new value in the table
        table = 'cause'
        colunm = 'description_cause'
        data_analyze = {
            'value': trouble.description_cause,
        }
        cursor.execute(f"SELECT IF (COUNT(*) > 0, 'exist', 'not_exist') FROM {table} WHERE {colunm} = %(value)s",
                       data_analyze)

        data = cursor.fetchall()
        exist = [str(x) for x, in data]

        if (exist[0] == 'not_exist'):
            data_cause = {
               'description_cause': trouble.description_cause,
            }
            cursor.execute(add_cause, data_cause)

        # insert resolution_method

        #check before if there is the value, if not, add a new value in the table
        table = 'resolution_method'
        colunm = 'description_resolution'
        data_analyze = {
            'value': trouble.description_resolution,
        }
        cursor.execute(f"SELECT IF (COUNT(*) > 0, 'exist', 'not_exist') FROM {table} WHERE {colunm} = %(value)s",
                       data_analyze)
        data = cursor.fetchall()
        exist = [str(x) for x, in data]

        if (exist[0] == 'not_exist'):

            data_resolution = {
               'description_resolution': trouble.description_resolution,
            }
            cursor.execute(add_resolution, data_resolution)

        # insert reference

        table = 'reference'
        colunm = 'description_reference'
        data_analyze = {
            'value': trouble.description_reference,
        }
        cursor.execute(f"SELECT IF (COUNT(*) > 0, 'exist', 'not_exist') FROM {table} WHERE {colunm} = %(value)s",
                       data_analyze)
        data = cursor.fetchall()
        exist = [str(x) for x, in data]

        if (exist[0] == 'not_exist'):

            data_reference = {
               'description_reference': trouble.description_reference,
            }
            cursor.execute(add_reference, data_reference)

        if (trouble.trouble_no):

            # update trouble_relation
            update_trouble_relation = ("UPDATE trouble_relation SET "
                                       "description_fault = %(description_fault)s, "
                                        "description_cause = %(description_cause)s, "
                                        "description_resolution = %(description_resolution)s, "
                                        "description_reference = %(description_reference)s "
                                        "WHERE trouble_no = %(trouble_no)s")
            # alter trouble_relation
            data_trouble_relation = {
                'description_fault': trouble.description_fault,
                'description_cause': trouble.description_cause,
                'description_resolution': trouble.description_resolution,
                'description_reference': trouble.description_reference,
                'trouble_no': trouble.trouble_no
            }
            cursor.execute(update_trouble_relation, data_trouble_relation)
        else:
            # insert trouble_relation
            data_trouble_relation = {
                'description_fault': trouble.description_fault,
                'description_cause': trouble.description_cause,
                'description_resolution': trouble.description_resolution,
                'description_reference': trouble.description_reference,
            }
            cursor.execute(add_trouble_relation, data_trouble_relation)
            trouble.trouble_no = cursor.lastrowid
        cnx.commit()
        # cursor.close()
        # cnx.close()
        return

    def listar(self):
        #cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_TROUBLE)
        troubles = traduz_trouble(cursor.fetchall())
        return troubles

    def buscar_por_trouble_no(self, trouble_no):
        #cursor = self.__db.cursor()
        cursor.execute(SQL_TROUBLE_POR_ID, (trouble_no,))
        tupla = cursor.fetchone()
        return Trouble_relation(tupla[1], tupla[2], tupla[3], tupla[4], trouble_no=tupla[0])

    def delete(self, trouble_no):

        cursor.execute(SQL_DELETE_TROUBLE, (trouble_no, ))
        cnx.commit()

        return

    def search_fault_no(self, former):
        data = {'description_fault': former,
                              }
        cursor.execute("SELECT fault_no FROM fault WHERE description_fault = %(description_fault)s", data)
        tupla = cursor.fetchone()


        return tupla[0]

        # tupla =[]
        # if cont == 0:
        #     # fault
        #     data = {'description_fault': former,
        #                       }
        #     cursor.execute("SELECT fault_no FROM fault WHERE description_fault = %(description_fault)s", data)
        #     tupla = cursor.fetchone()
        #
        # if cont == 1:
        #     #cause
        #     data = {'description_cause': former,
        #             }
        #     cursor.execute("SELECT cause_no FROM cause WHERE description_cause = %(description_cause)s", data)
        #     tupla = cursor.fetchone()
        #
        # if cont == 2:
        #     # resolution_method
        #     data = {'description_resolution': former,
        #             }
        #     cursor.execute("SELECT resolution_no FROM resolution_method WHERE description_resolution = %(description_resolution)s", data)
        #     tupla = cursor.fetchone()
        #
        # if cont == 3:
        #     # reference
        #     data = {'description_reference': former,
        #             }
        #     cursor.execute("SELECT reference_no FROM reference WHERE description_reference = %(description_reference)s", data)
        #     tupla = cursor.fetchone()





    def search_double(self):
        pass

class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def busca_por_fault_no(self, fault_no):
        cursor = self.__db.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_trouble(troubles):
    def cria_trouble_com_tupla(tupla):
        return Trouble_relation(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
    return list(map(cria_trouble_com_tupla, troubles))


def traduz_usuario(tupla):
    return User(tupla[0], tupla[1], tupla[2])


