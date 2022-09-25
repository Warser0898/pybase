'''
Return code references
0  A database with the same name as the newly added one already existed, a new name should be specified.
1  Execution succeeded.
'''

def createDb(db_name, row_name):
    f = open("database/db_stat", "r")
    header = f.readline()
    if header[0] == "n": # if the db_test is empty, rewrite the db_test.
        f.close()
        f = open("database/db_stat", "w")
        f.write("%s\n" % db_name)
        f.close()
        f = open("database/%s" % db_name, "a")
        i = 0
        while i < (len(row_name) - 1):
            f.writelines("%s," % row_name[i])
            i += 1
        f.writelines("%s\n" % row_name[-1])
        f.close()
        return 1
    else: # if the db_test contains information, then directly append new entries to it.
        try:
            f = open("database/db_stat", "r")
            check_result = f.readlines().index("%s\n" % db_name)

        except ValueError:
            f = open("database/db_stat", "a")
            f.write("%s\n" % db_name)
            f.close()
            f = open("database/%s" % db_name, "a")
            i = 0
            while i < (len(row_name) - 1):
                f.writelines("%s," % row_name[i])
                i += 1
            f.writelines("%s\n" % row_name[-1])
            f.close()
            return 1

        else: # if there's an entry using the same name as the newly added entry, throw error code 0.
            return 0






