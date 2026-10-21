"""任务查询与排序（组员 C 负责）。

只负责查询和计算，不修改原列表，不保存 JSON 文件。

需要完成的功能（接口约定见开发说明第 4 节 C）：
1. get_pending_tasks(tasks)：返回未完成任务的新列表。
2. get_completed_tasks(tasks)：返回已完成任务的新列表，
   完成时间新的排在前面。
3. sort_tasks(tasks, method)：method 只能是 "priority" 或 "deadline"；
   返回排序后的新列表，不改变原列表。
   - "priority"：P0 → P1 → P2；
   - "deadline"：截止时间从早到晚。
4. check_deadline(task)：返回下面四个值之一：
   - "completed"：任务已完成；
   - "overdue"：未完成且已超过截止时间；
   - "soon"：未完成且剩余时间在 0～24 小时之间（包括 24 小时）；
   - "normal"：其余情况。

时间解析统一使用 datetime.strptime(时间字符串, "%Y-%m-%d %H:%M")。
"""


def get_pending_tasks(tasks):
    # TODO（C）：在这里实现；返回未完成任务的新列表
    pass


def get_completed_tasks(tasks):
    # TODO（C）：在这里实现；返回已完成的新列表，最新完成在前
    pass


def sort_tasks(tasks, method):
    # TODO（C）：在这里实现；返回排序后的新列表，不修改原列表
    pass


def check_deadline(task):
    # TODO（C）：在这里实现；返回 completed / overdue / soon / normal
    pass
