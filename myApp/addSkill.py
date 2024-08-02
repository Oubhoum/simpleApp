import sqlite3
import commitClose

def add_skill(cr, uid, db):
    
    sk = input("Write Skill Name: ").strip().capitalize()
    
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")
    
    result = cr.fetchall()
    
    if result:
        print("skills is exists, you can't add it:")
        answer = input("do you would like to update progress: Y/N: ").strip().upper()
        if answer == "Y":

            prog = input("write the new skill progress ").strip()
            cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
        elif answer == "N":
            print("no change happend over your skills progress.")
    
    else:
        prog = input("Write Skill Progress: ").strip()
        cr.execute(
            f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
    commitClose.commit_and_close(db)