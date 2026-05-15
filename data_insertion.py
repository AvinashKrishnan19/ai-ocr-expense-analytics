import sqlite3
from parser import parse_multiple_invoice

DB_NAME = "ocr_master_table.db"
TABLE_NAME = "ocr_line_items"


def insert_extracted_data():

    con = None
    insert_count = 0

    try:

        con = sqlite3.connect(DB_NAME)

        cur = con.cursor()

        all_bill_data = parse_multiple_invoice()

        if not all_bill_data:
            print("No data found")
            return

        for bill_dict in all_bill_data:

            enriched_line_items = bill_dict.get("Description", [])

            for i, item_dict in enumerate(enriched_line_items):

                if not isinstance(item_dict, dict):
                    print("Skipping invalid line item")
                    continue

                data_tuple = (

                    bill_dict.get("Invoice_No"),

                    i + 1,

                    bill_dict.get("Issue_Date"),

                    bill_dict.get("billed_to"),

                    None,

                    item_dict.get("service_description"),

                    item_dict.get("category"),

                    item_dict.get("Amount"),

                    bill_dict.get("Grand_total"),

                    bill_dict.get("source_file")
                )

                cur.execute(f"""
                    INSERT OR REPLACE INTO {TABLE_NAME}
                    (
                        Invoice_No,
                        line_item_id,
                        Issue_Date,
                        billed_to,
                        billed_by,
                        Description,
                        Category,
                        Amount,
                        Grand_Total,
                        source_file
                    )

                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

                """, data_tuple)

                insert_count += 1

        con.commit()

        print(f"\nData insertion completed")
        print(f"Total inserted rows: {insert_count}")

    except sqlite3.Error as e:

        print(f"SQLite Error: {e}")

    except Exception as e:

        print(f"General Error: {e}")

    finally:

        if con:
            con.close()


if __name__ == "__main__":

    insert_extracted_data()

