import mysql.connector
import db_action
import db_structure
from mysql.connector import errorcode

class DataBaseStart():
    @classmethod
    def start(self):
        # Получение курсора
        cnx, cursor = db_action.DB.create_connection_without_db()

        def create_database():
            try:
                cursor.execute(
                    "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_structure.DB_NAME))
            except mysql.connector.Error as err:
                print("Failed creating database: {}".format(err))
                exit(1)

        # Создание БД и таблиц, сами таблицы в structure
        try:
            cursor.execute("USE {}".format(db_structure.DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(db_structure.DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database()
                print("Database {} created successfully.".format(db_structure.DB_NAME))
                cnx.database = db_structure.DB_NAME
            else:
                print(err)
                exit(1)

        for table_name in db_structure.TABLES:
            table_description = db_structure.TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        
        try:
            cursor.execute(db_structure.DATAS)
            cnx.commit()
        except mysql.connector.Error as err:
            print(err)
        # Закрываем курсор здесь же
        cursor.close()
        cnx.close()
        

