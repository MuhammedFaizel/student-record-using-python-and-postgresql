import psycopg2


def connect():

    conn = psycopg2.connect(
        database="studentrecord",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()
    return conn, cur


def create_table():

    conn, cur = connect()
    cur.execute(
        "CREATE TABLE student (roll_no INT PRIMARY KEY, name VARCHAR(10), english_mark INT, maths_mark INT)"
    )
    conn.commit()


def insert_data(roll_no, name, english_mark, maths_mark):

    conn, cur = connect()
    cur.execute(
        "INSERT INTO student VALUES(%s, %s, %s, %s)",
        (roll_no, name, english_mark, maths_mark),
    )
    conn.commit()


def fetch_data():

    conn, cur = connect()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    return data


def print_data(data):

    print("Query result: ")
    print()
    for row in data:

        print("roll_no", row[0])
        print("name: ", row[1])
        print("english_mark", row[2])
        print("maths_mark", row[3])
        print("----------------------------------")


def search_table(rollno):
    conn, cur = connect()
    cur.execute("SELECT * FROM student where roll_no =%s",rollno)
    data=cur.fetchall()
    for row in data:
        print("roll_no", row[0])
        print("name: ", row[1])
        print("english_mark", row[2])
        print("maths_mark", row[3])

def update_table(m_1,m_2,rollno):
    conn, cur = connect()
    pg_update = "UPDATE student set english_mark=%s ,maths_mark=%s where roll_no = %s"
    cur.execute(pg_update,(m_1,m_2,rollno))
    conn.commit()
    count = cur.rowcount
    print(count, "Successfully Updated!")

connect()
create_table()
while True:
    print("\nOperations")
    print("\n1. Add Student \n2. Display \n3. Serach \n4. Update \n5. Exit")
    print("\n")
    ch = int(input("Enter your operation: "))

    if ch == 1:
        s = int(input("How many Students have to be added: "))
        for i in range(s):
            n = input("Enter name: ")
            r = int(input("Enter the roll number: "))
            m_1 = int(input("Enter mark 1: "))
            m_2 = int(input("Enter mark 2: "))
            print("\n")
            insert_data(r, n, m_1, m_2)

    elif ch == 2:
        data = fetch_data()
        print_data(data)

    elif ch == 3:
        rollno = input("enter the roll no of student to be searched")
        search_table(rollno)

    elif ch == 4:
        rollno = input("enter the roll no of student whose data is to be updated :")
        m_1 = int(input("Enter mark 1: "))
        m_2 = int(input("Enter mark 2: "))
        update_table(rollno,m_1, m_2)

    elif ch == 5:
        break

    else:
        print("INvalid option")
        continue
    continue_next = input("Do you want to continue(Y/N): ").lower()
    if continue_next not in ["y", "yes"]:
        break

print("Thank you")



