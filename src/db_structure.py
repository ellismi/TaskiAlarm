import setting
# Задание БД и таблиц
DB_NAME = setting.db

TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `telegram_id` INTEGER UNIQUE NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ")")

TABLES['projects'] = (
    "CREATE TABLE `projects` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `user_id` INTEGER NOT NULL,"
    "  `project_name` VARCHAR(255) DEFAULT 'Входящие',"
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `user_project_fk_1` FOREIGN KEY (`user_id`) "
    "     REFERENCES `users` (`id`)"
    ")")

TABLES['users_projects'] = (
    "CREATE TABLE `users_projects` ("
    "  `user_id` INTEGER NOT NULL,"
    "  `project_id` INTEGER NOT NULL,"
    "  CONSTRAINT `user_project_fk_2` FOREIGN KEY (`user_id`) "
    "     REFERENCES `users` (`id`),"
    "  CONSTRAINT `user_project_fk_3` FOREIGN KEY (`project_id`) "
    "     REFERENCES `projects` (`id`)"
    ")")

TABLES['lists'] = (
    "CREATE TABLE `lists` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `list_name` VARCHAR(255) DEFAULT '.default',"
    "  `project_id` INTEGER NOT NULL,"
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `project_list_fk_1` FOREIGN KEY (`project_id`) "
    "     REFERENCES `projects` (`id`)"
    ")")


TABLES['tasks'] = (
    "CREATE TABLE `tasks` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `task_name` VARCHAR(255) NOT NULL,"
    "  `list_id` INTEGER NOT NULL,"
    "  `parent_id` INTEGER,"
    "  `tags` VARCHAR(255),"
    "  `status` INTEGER NOT NULL DEFAULT 0,"
    "  `scheduled` DATE NULL, "
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `list_task_fk_1` FOREIGN KEY (`list_id`) "
    "     REFERENCES `lists` (`id`)"
    ")")

TABLES['alarms'] = (
    "CREATE TABLE `alarms` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `type` INTEGER NOT NULL,"
    "  `count_interval` INTEGER,"
    "  `time_interval` INTEGER,"
    "  `day_interval` INTEGER,"
    "  `week_interval` INTEGER,"
    "  `month_interval` INTEGER,"
    "  `year_interval` INTEGER,"
    "  `task_id` INTEGER NOT NULL,"
    "  `status` INTEGER NOT NULL DEFAULT 0,"
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `task_alarm_fk_1` FOREIGN KEY (`task_id`) "
    "     REFERENCES `tasks` (`id`)"
    ")")

DATAS = (
    "CREATE TRIGGER projects_after_insert AFTER INSERT ON projects FOR EACH ROW BEGIN INSERT INTO users_projects (user_id, project_id) VALUES (NEW.user_id, NEW.id); INSERT INTO lists (project_id) VALUES (NEW.id); END;    CREATE TRIGGER users_after_insert AFTER INSERT ON users FOR EACH ROW BEGIN INSERT INTO projects (user_id, project_name) VALUES (NEW.id, DEFAULT); END  "
)
