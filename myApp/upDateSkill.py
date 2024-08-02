import sqlite3
import commitClose


def update_skill(cr, uid, db):
    sk = input("weite skill name: ").strip().capitalize()
    prog = input("write the new skill progress ").strip()
    
    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
    commitClose.commit_and_close(db)
    