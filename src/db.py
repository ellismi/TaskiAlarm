import db_action as action

class SQLCommand():
    @classmethod
    def add_user(self, telegram_id):
        query = 'SELECT id FROM users WHERE telegram_id = %(telegram_id)s'
        sqldata = {
            'telegram_id': telegram_id
        }
        data = action.DB.sql_select(query, sqldata)
        print(data)
        if data is None:
            query = 'INSERT INTO users (telegram_id) VALUES (%(telegram_id)s)'
            action.DB.sql_action(query, sqldata)
    
    @classmethod
    def add_task(self, task_name, list_id = 0):
        list_name = ''
        query = ''
        if (list_id == 0):
            list_name = '.default'
            query = 'select list_id from lists'
            action.DB.sql_select()
        
        
        query = 'INSERT INTO tasks (telegram_id) VALUES (%(telegram_id)s)'

    @classmethod 
    def show_all_tasks(self, telegram_id):
        query = (" SELECT tasks.id AS task_id, tasks.task_name AS task_name, tasks.status AS statuse, "
                " lists.id AS list_id, lists.list_name AS list_name, lists.project_id AS project_id, ui AS user_id "
                " FROM tasks  JOIN lists ON  (lists.id = tasks.list_id)  JOIN (SELECT projects.id AS pid, users.id AS ui "
                " FROM users, users_projects, projects"
                " WHERE users.id = users_projects.user_id AND projects.id = users_projects.project_id AND users.telegram_id=%(telegram_id)s) AS t "
                " ON (lists.project_id = t.pid);")
        sqldata = {
            'telegram_id': telegram_id
        }
        data = action.DB.sql_select(query, sqldata)
        print(data)

            


