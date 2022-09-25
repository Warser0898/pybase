'''
ManageDb is a class that includes the functions needed to change databases.
included functions are add_entry, update_entry, delete_entry, search_entry, list_db.
'''

class ManageDb:

    def __init__(self):
        pass

    def list_db():
        with open("database/db_stat", "r") as f:
            result_init = f.readlines()
            for i in result_init:
                print(i, end="")

    def add_entry(input_row, db_name):
        with open("database/%s" % db_name, "a") as f:
            n = len(input_row)
            q = 0
            while q < n - 1:
                f.write("%s," % input_row[q])
                q += 1
            f.write("%s\n" % input_row[-1])

    def update_one_element(x_str, y_str, new_value, db_name):
        x = int(x_str)
        y = int(y_str)

        with open("database/%s" % db_name, "r") as f:
            db_unchanged = f.readlines()
            changed_row_raw = db_unchanged[y]
            original_value = changed_row_raw.split(",")[x-1]
            changed_row = changed_row_raw.replace(original_value, new_value)
            db_unchanged.pop(y)
            db_changed_raw = db_unchanged
            db_changed_raw.insert(y, changed_row)
            db_changed = db_changed_raw

        with open("database/%s" % db_name, "w") as f:
            f.writelines(db_changed)

    def update_one_line(y_str, new_line, db_name):
        y = int(y_str)

        with open("database/%s" % db_name, "r") as f:
            db_unchanged = f.readlines()
            db_unchanged.pop(y)
            db_item_removed = db_unchanged
            db_item_removed.insert(y, new_line)
            db_changed = db_item_removed

        with open("database/%s" % db_name, "w") as f:
            f.writelines(db_changed)

    def delete_entry(y_str, db_name):
        y = int(y_str)

        with open("database/%s" % db_name, "r") as f:
            db_unchanged = f.readlines()
            db_unchanged.pop(int(y))
            db_changed = db_unchanged

        with open("database/%s" % db_name, "w") as f:
            f.writelines(db_changed)

    def search_db(key_word, db_name):
        with open("database/%s" % db_name, "r") as f:
            result_get = f.readlines()
            result_pool = []
            for line in result_get:
                result_quantified = line.split(",")
                result_pool.append(result_quantified)
            result_pool.pop(0)
            row_count = 1
            row_target_located = []
            for each in result_pool:
                each_result = each.count(str(key_word))
                if each_result > 0:
                    row_target_located.append(row_count)
                row_count += 1

            return row_target_located

    def get_db_header(db_name):
        with open("database/%s" % db_name, "r") as f:
            header = f.readline()
            return header

    def return_a_certain_line(y, db_name):
        with open("database/%s" % db_name, "r") as f:
            all_lines = f.readlines()
            return all_lines[y]

    def remove_db(db_name):
        import os
        with open("database/db_stat", "r") as f:
            db_list = f.readlines()
            target_position = db_list.index(db_name + "\n")
            ManageDb.delete_entry(target_position, "db_stat")

        os.remove("database/%s" % db_name)








    



