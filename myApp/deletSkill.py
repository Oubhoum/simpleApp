import sqlite3
import commitClose

def delete_skill(cr, uid, db):
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    commitClose.commit_and_close(db)
    
