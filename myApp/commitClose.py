import sqlite3

def commit_and_close(db):
    """commit changes close data base"""
    db.commit()
    db.close()
    print("Connection To Database Is Closed")
