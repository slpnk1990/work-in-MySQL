import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected")
    print('#' * 20)

    try:
        #создание таблицы
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `toys`(id int AUTO_INCREMENT," \
        #                          "toy_id varchar(32), PRIMARY KEY (id)," \
        #                          "name varchar(32)," \
        #                          "status varchar(32)," \
        #                          "status_updated varchar(32));"
        #     cursor.execute(create_table_query)
        #     print("Table created!")


        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `games`(id int AUTO_INCREMENT," \
        #                          "game_id varchar(32), PRIMARY KEY (id)," \
        #                          "name varchar(32)," \
        #                          "date varchar(32));"
        #     cursor.execute(create_table_query)
        #     print("Table created!")

        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `toys_games`(id int AUTO_INCREMENT," \
        #                          "game_id varchar(32), PRIMARY KEY (id)," \
        #                          "toy_id varchar(32)," \
        #                          "note varchar(32));"
        #     cursor.execute(create_table_query)
        #     print("Table created!")

        # # добавление данных в таблицу
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `toys` (toy_id, name, status, status_updated) VALUES('1', 'boat', 'broken', '2018-03-19');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `toys` (toy_id, name, status, status_updated) VALUES('7', 'Teddy Bear', 'ok', '2018-03-30');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `toys` (toy_id, name, status, status_updated) VALUES('43', 'octopus', 'ok', '2018-03-19');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `games` (game_id, name, date) VALUES('1', 'Ships in the ocean', '2018-02-12');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `games` (game_id, name, date) VALUES('5', 'ZOO Railroad', '2018-03-30');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `games` (game_id, name, date) VALUES('14', 'Octopus-destroyer', '2018-03-18');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # # обновление данных в таблице
        # with connection.cursor() as cursor:
        #     update_query = "UPDATE `toys` SET status = 'ok' WHERE id = '2';"
        #     cursor.execute(update_query)
        #     connection.commit()


        # # удалине данных из таблицы
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `toys` WHERE id = 2;"
        #     cursor.execute(delete_query)
        #     connection.commit()


        # # удаление всей таблицы
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `toys`;"
        #     cursor.execute(drop_table_query)


        #запрос данных из таблицы
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `toys`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#" * 20)
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)