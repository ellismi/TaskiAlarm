import mysql.connector
import setting

class DB():
    @classmethod
    def create_connection(self):
        # Открытие подключения
        self.cnx = mysql.connector.connect(user=setting.user, password=setting.password,
                              host=setting.host,
                              database=setting.db)
        self.cursor = self.cnx.cursor()
        print('has connection')
        return self.cnx, self.cursor

    @classmethod
    def sql_action(self, query, data =''):
        cnx, cursor = self.create_connection()    
        answer = ''    
        # Если есть данные для запроса подаем их 
        try:
            if (data):
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            cnx.commit()
        except mysql.connector.Error as err:
            print("{}".format(err))
        answer = cursor.lastrowid
        cursor.close()
        cnx.close()
        return answer

    @classmethod
    def sql_select(self, query, data =''):
        cnx, cursor = self.create_connection()
        answer = []
        try:
            if (data):
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                return None
            while row is not None:
                answer.append(row)
                row = cursor.fetchone()
        except mysql.connector.Error as err:
            print("error {}".format(err))
        
        cursor.close()
        cnx.close()
        return answer
    
       
        