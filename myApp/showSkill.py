import sqlite3
import commitClose


def show_skills(cr, uid, db):
    cr.execute(f"select * from skills where user_id = '{uid}'")
    
    result = cr.fetchall()
    
    print(f"you have {len(result)} skills.")
    
    if len(result):
        print("showing skills with progress: ")
        for row in result:
            print(f"skill => {row[0]}, ", end=" ")
            print(f"progress => {row[1]}%")
    else:
        print(f"the user number {uid} has no skill")
    commitClose.commit_and_close(db)
    
