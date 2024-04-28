from connectToMssql import database_


db = database_(server="DESKTOP-PLFHE01\SQLEXPRESS", database="testSql")
if db.connectToDatabase(4):

    name_table = "Students"
    columns = [
        "ID INT PRIMARY KEY",
        "Name VARCHAR(50)",
        "Email VARCHAR(50)",
        "Age INT",
        "Graduated DATE"
    ]

    db.createTable(name_table, columns)

    db.writeToTable(name_table, 1, "Zeynep KILIC", "zeynp@gmail.com", 25, "2020-7-10")
    db.writeToTable(name_table, 2, "Sedef SAKİR", "sedef@gmail.com", 23, "2022-8-9")
    db.writeToTable(name_table, 3, "Büşra Nur Çelik", "bnur@gmail.com", 26, "2022-8-5")
    db.writeToTable(name_table, 4, "Dilara Tanal", "dlara@gmail.com", 24, "2020-7-20")
    db.writeToTable(name_table, 5, "Ayse Nur", "aysenr@gmail.com", 22, "2022-7-25")
    db.writeToTable(name_table, 6, "Cemile Genc", "cemile@gmail.com", 21, "2022-7-15")
    db.writeToTable(name_table, 7, "Elif Sezen", "elif@gmail.com", 22, "2022-7-25")
    db.writeToTable(name_table, 8, "Merve Deniz", "mrve@gmail.com", 27, "2020-7-16")
    db.writeToTable(name_table, 9, "Aslı Çakmak", "asli@gmail.com", 23, "2021-8-2")
    db.writeToTable(name_table, 10, "Sıla Aydın", "sila@gmail.com", 18, "2021-6-25")

    db.readFromTable(name_table, "all")
    # db.readFromTable(name_table, "rows", number=4)
    # db.readFromTable(name_table, "range", key="Age", value=25)
    # db.readFromTable(name_table, "date", key='Graduated', value='2021-6-25')

    # db.readFromTable(name_table, "specific", Age=22, Graduated="2022-7-25")

    # db.deleteFromTable(name_table, "all")
    # db.deleteFromTable(name_table, "one_col", "Age")
    # db.deleteFromTable(name_table, "some_rows", key="Age", value=21)
    #db.deleteFromTable(name_table, "specific", key="ID", value=10)

    # db.deleteTable(name_table)
    db.closeCursor()


else:
    pass


