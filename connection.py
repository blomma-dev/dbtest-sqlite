import sqlite3


db_name = 'blomma.db'

def Add_user(cursor, connection):
    user_name = input('Enter username: ')
    account_type = input('Enter account type: ')
    
    i = 0
    sql = "SELECT id, name FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    i = result[-1][0] + 1

    username_exists = any(user_name == row[1] for row in result)

    if username_exists:
        print("User exist!\n")

    else:    
        sql = "INSERT INTO users (id, name, type) VALUES (?, ?, ?)"
        cursor.execute(sql, (i, user_name, account_type))

        cursor.close()
        connection.commit()

        print("Record inserted successfully into database.\n")

    return


def Main():
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        print('Connection to SQLite DB successful\n')

        while True:
            command = input("What do you want to do?\nAdd\nQuit\n\n")
            
            if(command == "Add"):
                Add_user(cursor, connection)
                
            elif(command == "Quit"):
                print("Bye!")
                break

            else:
                print("Unknown command!\n")
        
        
    except Exception as e:
        print("An error occurred, and it is your fault.", e)
        if connection:
            connection.close()

Main()