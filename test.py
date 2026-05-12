import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Root@123",
        auth_plugin='mysql_native_password'
    )

    print("CONNECTED SUCCESSFULLY")

except Exception as e:
    print(e)