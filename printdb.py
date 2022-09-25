'''
this module contains the functions needed to correctly display the databases.
'''

def print_db(db_name):
    with open("database/%s" % db_name, "r") as f:
        display = f.readlines()
        line = 0
        for i in display:
            if line == 0:
                out = "   " + i
                print(out, end="")
            else:
                out = str(line) + "  " + i
                print(out, end="")

            line += 1





