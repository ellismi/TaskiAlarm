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
    def add_task(self, task_name, list_id):
        query = ("INSERT INTO tasks (task_name, list_id) "
        "VALUES (%(task_name)s, %(list_id)s);")
        sqldata = {
            'task_name': task_name,
            'list_id': list_id
        }
        return action.DB.sql_action(query, sqldata)

    @classmethod 
    def show_all_tasks(self, telegram_id):
        query = (" SELECT tasks.id AS task_id, tasks.task_name AS task_name, tasks.status AS statuse, "
                " lists.id AS list_id, lists.list_name AS list_name, lists.project_id AS project_id, ui AS user_id "
                " FROM tasks  JOIN lists ON  (lists.id = tasks.list_id) JOIN (SELECT projects.id AS pid, users.id AS ui "
                " FROM users, users_projects, projects"
                " WHERE users.id = users_projects.user_id AND projects.id = users_projects.project_id AND users.telegram_id=%(telegram_id)s) AS t "
                " ON (lists.project_id = t.pid);")
        sqldata = {
            'telegram_id': telegram_id
        }
        data = action.DB.sql_select(query, sqldata)
        print(data)
        return data 
    @classmethod
    def add_project(self, telegram_id, project_name):
        query = ("INSERT INTO projects (user_id, project_name) "
                "VALUES ((SELECT id FROM users WHERE telegram_id = %(telegram_id)s), %(project_name)s);")
        sqldata = {
            'telegram_id': telegram_id,
            'project_name': project_name
        }
        return action.DB.sql_action(query, sqldata)
        # print(data)

    @classmethod
    def add_list(self, project_id, list_name):
        query = ("INSERT INTO lists (project_id, list_name) "
                "VALUES (%(project_id)s, %(list_name)s);")
        sqldata = {
            'project_id': project_id,
            'list_name': list_name
        }
        return action.DB.sql_action(query, sqldata)
        # print(data)

    @classmethod 
    def show_project(self, telegram_id):
        query = ("SELECT projects.project_name, projects.id "
            "FROM users, users_projects, projects "
            "WHERE users.id = users_projects.user_id "
            "AND projects.id = users_projects.project_id "
            "AND users.telegram_id = %(telegram_id)s;")
        sqldata = {
            'telegram_id': telegram_id
        }
        data = action.DB.sql_select(query, sqldata)
        return data 

    @classmethod 
    def show_lists(self, project_id):
        query = ("SELECT lists.list_name, lists.id "
            "FROM lists "
            "WHERE lists.project_id = %(project_id)s;")
        sqldata = {
            'project_id': project_id
        }
        data = action.DB.sql_select(query, sqldata)
        return data 

    @classmethod 
    def use_def_list(self, telegram_id):
        query = ("SELECT lists.id FROM projects, users, lists WHERE users.telegram_id = %(telegram_id)s AND users.id = projects.user_id AND lists.project_id = projects.id AND projects.project_name='Входящие';")
        sqldata = {
            'telegram_id': telegram_id
        }
        data = action.DB.sql_select(query, sqldata)
        return data[0][0]

    @classmethod
    def show_task_list(self, telegram_id):

        list_id = self.use_def_list(telegram_id)
        print(list_id)
        query = ("SELECT task_name, id "
                " FROM tasks WHERE list_id = %(list_id)s AND status = 0;")
        sqldata = {
            'list_id': list_id
        }
        data = action.DB.sql_select(query, sqldata)
        return data 

