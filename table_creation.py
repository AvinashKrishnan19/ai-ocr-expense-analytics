import sqlite3

DB_NAME = "ocr_master_table.db"

con= None

try:
    con =sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        create table if not exists ocr_line_items(
                Invoice_No TEXT NOT NULL,
                line_item_id INTEGER NOT NULL,
                Issue_Date TEXT,
                billed_to TEXT,
                billed_by TEXT,
                Description TEXT,
                Category TEXT,
                Amount REAL,
                Grand_Total REAL,
                source_file TEXT, -- column name case for consistency
                PRIMARY KEY (Invoice_No, line_item_id)
                )
                """)
    
    con.commit()
    print(f"table successfully created")

except sqlite3.Error as e:
    print(f"error is {e}")

finally:
    if con:
        con.close()




