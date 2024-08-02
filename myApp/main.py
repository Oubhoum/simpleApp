
import sqlite3
import showSkill
import addSkill
import deletSkill
import upDateSkill
import commitClose
import myString as mst

db = sqlite3.connect("app.db")
cr = db.cursor()

uid = 1

input_message = mst.my_str

# input option choose
user_input = input(input_message).strip().lower()

# command list
command_list = ["s", "a", "d", "u", "q"]

if user_input not in command_list:
    print(f"commnad {user_input} not fond in {command_list}")
else:
    if user_input == "s":
        showSkill.show_skills(cr, uid, db)
    elif user_input == "a":
        addSkill.add_skill(cr, uid, db)
    elif user_input == "d":
        deletSkill.delete_skill(cr, uid, db)
    elif user_input == "u":
        upDateSkill.update_skill(cr, uid, db)
    else:
        print("App is Closed.")
        commitClose.commit_and_close(db)