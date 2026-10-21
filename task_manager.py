"""任务管理（组员 B 负责）。

四个函数都直接修改传入的 tasks 列表，并统一返回 (success, message)，
例如 (True, "Task added") 或 (False, "Task not found")。
本模块不负责保存文件；保存由 main.py 调用 storage.save_tasks() 完成。

统一数据格式（见开发说明第 5 节）：
{
    "id": 1,
    "title": "Finish Python homework",
    "priority": "P0",
    "deadline": "2026-10-25 18:00",
    "completed": False,
    "completed_at": None
}

需要完成的功能：
1. add_task(tasks, title, priority, deadline)：
   - 校验：标题非空、priority 是 "P0"/"P1"/"P2"、
     deadline 能被 datetime.strptime(deadline, "%Y-%m-%d %H:%M") 解析。
   - 新任务 id 取现有任务的最大 id 加 1（保证当前列表内不重复）。
   - completed 为 False，completed_at 为 None。
2. edit_task(tasks, task_id, title=None, priority=None, deadline=None)：
   按 id 查找任务，只修改参数中不为 None 的字段；
   找不到任务或校验失败时返回 (False, 原因)。
3. complete_task(tasks, task_id)：
   把 completed 改为 True，completed_at 记录当前时间
   （格式 "YYYY-MM-DD HH:MM"）；已经完成的任务不要重复改时间。
4. delete_task(tasks, task_id)：按 id 删除，找不到返回 (False, ...)。
"""


def add_task(tasks, title, priority, deadline):
    # TODO（B）：在这里实现；校验输入 → 生成新 id → 加入列表 → 返回 (True, ...)
    pass


def edit_task(tasks, task_id, title=None, priority=None, deadline=None):
    # TODO（B）：在这里实现；按 id 查找并修改 → 返回 (success, message)
    pass


def complete_task(tasks, task_id):
    # TODO（B）：在这里实现；记录完成时间 → 返回 (success, message)
    pass


def delete_task(tasks, task_id):
    # TODO（B）：在这里实现；按 id 删除 → 返回 (success, message)
    pass
