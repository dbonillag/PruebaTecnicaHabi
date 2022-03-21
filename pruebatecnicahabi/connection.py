from mysql.connector import connect


def get_connection() -> object:
    """
    mysql database connection
    :return:
    """
    connection = connect(
        host="3.130.126.210",
        user="pruebas",
        password="VGbt3Day5R",
        port='3309',
        database="habi_db",

    )
    return connection
