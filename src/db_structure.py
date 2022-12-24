# Задание БД и таблиц
DB_NAME = 'mytasks'

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

TABLES['statuses'] = (
    "CREATE TABLE `statuses` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `status_name` VARCHAR(255) NOT NULL,"
    " PRIMARY KEY (`id`)"
    ")")
    
TABLES['tasks'] = (
    "CREATE TABLE `tasks` ("
    "  `id` INTEGER NOT NULL AUTO_INCREMENT,"
    "  `task_name` VARCHAR(255) NOT NULL,"
    "  `list_id` INTEGER NOT NULL,"
    "  `parent_id` INTEGER,"
    "  `tags` VARCHAR(255),"
    "  `status_id` INTEGER NOT NULL DEFAULT 0,"
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `list_task_fk_1` FOREIGN KEY (`list_id`) "
    "     REFERENCES `lists` (`id`),"
    "  CONSTRAINT `status_task_fk_2` FOREIGN KEY (`status_id`) "
    "     REFERENCES `statuses` (`id`)"
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
    "  `status_id` INTEGER NOT NULL DEFAULT 0,"
    "  PRIMARY KEY (`id`), "
    "  CONSTRAINT `task_alarm_fk_1` FOREIGN KEY (`task_id`) "
    "     REFERENCES `tasks` (`id`),"
    "  CONSTRAINT `status_alarm_fk_2` FOREIGN KEY (`status_id`) "
    "     REFERENCES `statuses` (`id`)"
    ")")
