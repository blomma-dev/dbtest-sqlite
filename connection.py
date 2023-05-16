import sqlite3


db_name = 'blomma.db'

def Add_user(cursor, connection):
    user_name = input('Enter username: ')
    account_type = input('Enter account type: ')
    
    i = 0
    sql = "SELECT id, name FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        i = 1
    else:
        i = result[-1][0] + 1

    username_exists = any(user_name == row[1] for row in result)

    if username_exists:
        print("User exist!\n")

    else:    
        sql = "INSERT INTO users (id, name, type) VALUES (?, ?, ?)"
        cursor.execute(sql, (i, user_name, account_type))
        connection.commit()


        print("Record inserted successfully into database.\n")

    return

def Read_users(cursor):
    sql = "SELECT id, name, type FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Users:")
    for row in result:
        print("-" + row[1] + ":" + row[2])
    print("\n")
    return
    

def Main():
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        print('Connection to SQLite DB successful\n')

        while True:
            command = input("What do you want to do?\nAdd:Read:Quit\n\n").lower()
            
            if(command == "add"):
                Add_user(cursor, connection)
            
            elif(command == "read"):
                Read_users(cursor)
                
            elif(command == "quit"):
                print("Bye!")
                cursor.close()
                break

            else:
                print("Unknown command!\n")
        
        
    except Exception as e:
        print("An error occurred, and it is your fault. The error message is: ", e)
        if connection:
            connection.close()

Main()