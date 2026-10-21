"""终端交互（组员 A 负责）。

职责：显示菜单、读取用户输入、调用 B/C/D 的函数、显示结果。
不要在这里重新编写添加、排序或保存文件的逻辑，只负责调用。

需要完成的功能：
1. show_menu()：用 print() 打印主菜单（菜单样式见开发说明第 6 节）：
      1. Add a task
      2. View tasks
      3. Edit a task
      4. Complete a task
      5. Delete a task
      6. View completed tasks
      7. Sort tasks
      0. Exit
2. display_tasks(tasks)：把任务列表逐行打印到终端；对每个未完成任务，
   调用 task_utils.check_deadline(task)，结果不是 "normal" 时给出提示。
3. main()：
   - 调用 storage.load_tasks() 读取数据；返回 None（文件损坏）时提示并退出。
   - 用 while 循环显示菜单并读取 input()。
   - 按用户选择调用对应函数：
       1 → input() 收集信息 → task_manager.add_task()
       2 → display_tasks(task_utils.get_pending_tasks(tasks))
       3 → input() 收集编号和要改的项 → task_manager.edit_task()
       4 → task_manager.complete_task()
       5 → task_manager.delete_task()
       6 → display_tasks(task_utils.get_completed_tasks(tasks))
       7 → input() 选择 priority/deadline → task_utils.sort_tasks()
       0 → 退出循环
   - 每次成功修改数据（增、改、完成、删除）后调用 storage.save_tasks(tasks)。
   - 保存失败时提示用户“已修改但未保存”。
   - 错误输入（如菜单输入 9、任务编号不存在）要提示并允许继续操作。

可以按开发说明第 7 节的示例组织代码。
"""


def show_menu():
    # TODO（A）：在这里实现；打印主菜单
    pass


def display_tasks(tasks):
    # TODO（A）：在这里实现；逐行打印任务，并用
    # task_utils.check_deadline(task) 提示逾期或 24 小时内到期
    pass


def main():
    # TODO（A）：在这里实现；读取数据 → 循环显示菜单 → 调用其他模块
    pass


if __name__ == "__main__":
    main()
