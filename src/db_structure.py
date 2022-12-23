# Задание БД и таблиц
DB_NAME = 'alarms'

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
    "  `project_name` VARCHAR(255) DEFAULT '.default',"
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
    "  `status` INTEGER NOT NULL,"
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
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `task_alarm_fk_1` FOREIGN KEY (`task_id`) "
    "     REFERENCES `tasks` (`id`)"
    ")")

TABLES['complete_tasks'] = (
    "CREATE TABLE `complete_tasks` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `task_id` INTEGER NOT NULL,"
    "  `lead_time` DATETIME NOT NULL,"
    "  `status` INTEGER,"
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `complete_task_fk_1` FOREIGN KEY (`task_id`) "
    "     REFERENCES `tasks` (`id`)"
    ")")

TABLES['complete_alarms'] = (
    "CREATE TABLE `complete_alarms` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `alarm_id` INTEGER NOT NULL,"
    "  `notice_time` DATETIME NOT NULL,"
    "  `status` INTEGER,"
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `complete_alarm_fk_1` FOREIGN KEY (`alarm_id`) "
    "     REFERENCES `alarms` (`id`)"
    ")")