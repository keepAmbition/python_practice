﻿**test**
```
 - **case1:学生视图**

-------------------------------------------------------------------------
                             选课系统

时间:11:57:51                                               今天:2017-07-31
-------------------------------------------------------------------------
【1】学员视图       【2】讲师视图      【3】管理视图        【4】退出系统

输入你的选择1

-------------------------------------------------------------------------
                             学员视图

时间:11:57:51                                           今天:2017-07-31
-------------------------------------------------------------------------
【1】学员注册       【2】上交学费      【3】选择班级        【4】退出系统

请选择：1
student_name:李琦
student_school:oldboy_北京
student_class:1班
password12345
2017-07-31 11:58:51,270 - test.log - INFO - 学生李琦注册成功

-------------------------------------------------------------------------
                             学员视图

时间:11:57:51                                           今天:2017-07-31
-------------------------------------------------------------------------
【1】学员注册       【2】上交学费      【3】选择班级        【4】退出系统

请选择：2
please input student account:1002
please input student password:12345
2017-07-31 11:59:06,176 - test.log - INFO - 学生编号1002不存在

-------------------------------------------------------------------------
                             学员视图

时间:11:57:51                                           今天:2017-07-31
-------------------------------------------------------------------------
【1】学员注册       【2】上交学费      【3】选择班级        【4】退出系统

请选择：2
please input student account:1001
please input student password:12345
2017-07-31 11:59:26,943 - test.log - INFO - 学生编号1001，登陆成功
please choice course:python
请输入你的学生编号：1001
2017-07-31 11:59:44,230 - test.log - INFO - 课程python需缴纳学费11000元！
请缴纳学费：11000

2017-07-31 11:59:50,577 - test.log - INFO - 课程python缴纳学费成功！
-------------------------------------------------------------------------
                             学员视图

时间:11:57:51                                           今天:2017-07-31
-------------------------------------------------------------------------
【1】学员注册       【2】上交学费      【3】选择班级        【4】退出系统

请选择：3
请输入你的学生编号：1001
请输入选择的班级：2班
2017-07-31 12:00:06,467 - test.log - INFO - 学生1001从班级1班调整至班级2班!

-------------------------------------------------------------------------
                             学员视图

时间:11:57:51                                           今天:2017-07-31
-------------------------------------------------------------------------
【1】学员注册       【2】上交学费      【3】选择班级        【4】退出系统

请选择：4
Process finished with exit code 1


 - **case2:讲师视图**

请输入你想选择教授的班级：1班
2017-07-31 13:11:15,952 - test.log - INFO - 选择班级成功,1班授课讲师已从AAAA更换成新讲师TTTT

-------------------------------------------------------------------------
                             讲师视图

时间:13:10:57                                           今天:2017-07-31
-------------------------------------------------------------------------
【1】选择班级上课                   【2】查看学员列表
【3】确定学员成绩                   【4】退出

请选择：2
请输入你所在学校名称：oldboy_北京
请输入你想查看学生明细的班级：1班
——————学生明显如下——————
张三
李四
舞王
阿斯顿

-------------------------------------------------------------------------
                             讲师视图

时间:13:10:57                                           今天:2017-07-31
-------------------------------------------------------------------------
【1】选择班级上课                   【2】查看学员列表
【3】确定学员成绩                   【4】退出

请选择：3
请输入你想打分的学生：王五
请输入该学生成绩：A
2017-07-31 13:12:09,484 - test.log - INFO - 打分成功,给学生王五打分为:A

-------------------------------------------------------------------------
                             讲师视图

时间:13:10:57                                           今天:2017-07-31
-------------------------------------------------------------------------
【1】选择班级上课                   【2】查看学员列表
【3】确定学员成绩                   【4】退出

请选择：4




 - **case3:管理视图**

-------------------------------------------------------------------------
                             选课系统

时间:13:17:08                                               今天:2017-07-31
-------------------------------------------------------------------------
【1】学员视图       【2】讲师视图      【3】管理视图        【4】退出系统

输入你的选择3

-------------------------------------------------------------------------
                             管理视图

时间:13:17:08                                          今天:2017-07-31
-------------------------------------------------------------------------
【1】创建讲师       【2】创建课程      【3】创建班级
【4】创建校区       【5】退出

请选择：1
teacher_name:BBBB
teacher_salary:10000
teacher_school:oldboy_北京
2017-07-31 13:17:44,638 - test.log - INFO - 创建讲师BBBB成功

-------------------------------------------------------------------------
                             管理视图

时间:13:17:08                                          今天:2017-07-31
-------------------------------------------------------------------------
【1】创建讲师       【2】创建课程      【3】创建班级
【4】创建校区       【5】退出

请选择：2
course name:java
course tuition:4
course cycle:5
2017-07-31 13:18:02,576 - test.log - INFO - 创建课程java成功

-------------------------------------------------------------------------
                             管理视图

时间:13:17:08                                          今天:2017-07-31
-------------------------------------------------------------------------
【1】创建讲师       【2】创建课程      【3】创建班级
【4】创建校区       【5】退出

请选择：3
classroom_name:8班
classroom_course:python
classroom_teacher:TTTT
2017-07-31 13:18:36,686 - test.log - INFO - 创建班级-8班成功

-------------------------------------------------------------------------
                             管理视图

时间:13:17:08                                          今天:2017-07-31
-------------------------------------------------------------------------
【1】创建讲师       【2】创建课程      【3】创建班级
【4】创建校区       【5】退出

请选择：4
school name:oldboy_上海
school place:上海
{'school': {'oldboy_北京': {'school place': '北京'}, 'oldboy_上海': {'school place': '上海'}}}
2017-07-31 13:18:56,794 - test.log - INFO - 创建学校oldboy_上海成功

-------------------------------------------------------------------------
                             管理视图

时间:13:17:08                                          今天:2017-07-31
-------------------------------------------------------------------------
【1】创建讲师       【2】创建课程      【3】创建班级
【4】创建校区       【5】退出

请选择：5
```