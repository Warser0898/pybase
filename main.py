# 程序包括：数据库创建 写入 修改 查询
# create_db list_db db_action
# 数据库输入检查 搜索找不到结果时提示没有结果

import createdb
import managedb
import printdb

print("\n欢迎使用本数据库软件!\n")
while True:
    menu_stat = 1

    print("(1) 创建数据库\n(2) 操作数据库\n(3) 管理数据库\n(4) 关于本软件\n(5) 退出\n请输入代号以执行相关功能")
    ui_input = input("请输入：")
    if ui_input == "1":
        ui_db_name = input("请输入数据库名称（请不要与现有数据库重名）：")
        n = 1
        row_name = []
        while True:
            ui_input = input("请输入第%d列的名称，若想终止输入，请输入\"e\"：" % n)
            if ui_input == "e":
                break
            row_name.append(ui_input)
            n += 1
        result = createdb.createDb(ui_db_name, row_name)
        if result == 0:
            print("已存在同名数据库，请重新为数据库命名。")
        if result == 1:
            print("数据库创建成功！")

    if ui_input == "2":
        while menu_stat == 1:

            print("----------以下是可供操作的数据库---------\n")
            managedb.ManageDb.list_db()
            ui_input = input("请选你要操作的数据库（输入名称）：")
            db_name = ui_input
            print("----------请选择要进行的操作----------\n（1）增添行   （2）删除行\n（3）更新某个元素 （4）更新某一行\n（5）搜索数据库 （6）浏览数据库\n（7）退出")
            ui_input_1 = input("请选你要进行的操作（输入序号）：")

            if ui_input_1 == "1":
                header = managedb.ManageDb.get_db_header(db_name)
                print("数据库的格式为：%s" % header)
                input_row_raw = input("请按照\"数据1 数据2 数据3\"的格式输入数据（数据与数据间以一个空格隔开）")
                input_row = input_row_raw.split(" ")
                managedb.ManageDb.add_entry(input_row, db_name)
                print("添加成功！")

            if ui_input_1 == "2":
                print("----------以下为数据库内容----------")
                printdb.print_db(db_name)
                print("\n")
                ui_input_2 = input("请输入你要删除的行对应的序号：")
                managedb.ManageDb.delete_entry(ui_input_2, db_name)
                print("删除成功！")

            if ui_input_1 == "3":
                print("----------以下为数据库内容----------")
                printdb.print_db(db_name)
                print("\n")
                ui_input_3 = input("请输入你要更改的元素所在的行数：")
                ui_input_4 = input("请输入你要更改的元素所在的列数（从左往右数）：")
                ui_input_5 = input("请输入更改后的内容：")
                managedb.ManageDb.update_one_element(ui_input_4, ui_input_3, ui_input_5, db_name)
                print("更改成功！")

            if ui_input_1 == "4":
                print("----------以下为数据库内容----------")
                printdb.print_db(db_name)
                print("\n")
                ui_input_6 = input("请输入你要更改的元素所在的行数：")
                ui_input_7 = input("请按照\"数据1 数据2 数据3\"的格式输入数据（数据与数据间以一个空格隔开）")
                input_row_1 = ui_input_7.replace(" ", ",")
                managedb.ManageDb.update_one_line(ui_input_6, input_row_1, db_name)
                print("更改成功！")

            if ui_input_1 == "5":
                ui_input_8 = input("请输入你要查找的内容：")
                result_line = managedb.ManageDb.search_db(ui_input_8, db_name)
                print("----------以下为关键字所在的行----------")
                for each in result_line:
                    search_result = managedb.ManageDb.return_a_certain_line(each, db_name)
                    print(search_result)

            if ui_input_1 == "6":
                print("----------以下为数据库内容----------")
                printdb.print_db(db_name)

            if ui_input_1 == "7":
                menu_stat = 0

    if ui_input == "3":
        print("（1）删除数据库")
        ui_input_9 = input("请输入选项对应的序号：")

        if ui_input_9 == "1":
            print("----------以下是可供操作的数据库----------")
            managedb.ManageDb.list_db()
            db_name = input("请输入要删除的数据库名称：")
            ui_input_11 = input("是否确认删除数据库 %s ？该操作不可逆。确认操作请输入\"y\"，否则输入除y之外的任何字符退出。" % db_name)
            if ui_input_11 == "y":
                managedb.ManageDb.remove_db(db_name)
                print("删除成功！")

    if ui_input == "4":
        with open("readme.md", "r") as f:
            readme = f.readlines()
            for line in readme:
                print(line)

    if ui_input == "5":
        print("再见！")
        exit(0)





























