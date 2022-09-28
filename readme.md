pybase是一款基于python的简易数据库，具备创建新数表，增添、删除行，修改行，搜索等功能。
目前功能尚在完善中，欢迎大家提出意见。

本数据库的核心组件为managedb.py, createdb.py, 包含了操作数据库要用到的函数。数据库的存放文件夹为database，
其中的db_stat是用来记录存在的数据库的表，为保证数据库能正常工作，建议不要随意修改该表。

本数据库还提供了交互式操作界面（main.py）。

Pybase is a simple database based on python. It is able to create new databases, add/remove/
change lines and search entries in databases.

Pybase is still growing and your suggestions are very welcomed.

The core of this database is managedb.py, createdb.py, which includes the functions needed to
operate the database. Databases are stored in the folder database. The db_stat in the folder
are responsible for keeping an account of exsisting databeses. To ensure that the database work
properly, do not modify it if you don't know what you are doing.

Pybase also offers an interactive interface (main.py).

相较mysql，pybase拥有更高的数据插入速度。插入10000，50000,100000条数据时，mysql分别耗时17.32，89.63，175.16秒，
而pybase仅耗时3.32，14.61，29.68秒。

Compared with mysql, pybase has a higher data insertion speed. In inserting 10 000, 50 000, 100 000 lines, 
mysql respectively takes 17.32, 89.63, 175.16 seconds, while pybase only takes 3.32, 14.61, 29.68 seconds.
