"""数据读写（组员 D 负责）。

只负责 tasks.json 的读写，不负责添加、删除或排序任务。

需要完成的功能（接口约定见开发说明第 4 节 D）：
1. load_tasks()：
   - 使用 json.load() 读取本文件同级的 tasks.json；
   - 文件不存在时返回空列表 []；
   - 文件存在但内容损坏（JSON 解析失败）时打印错误信息并返回 None。
2. save_tasks(tasks)：
   - 使用 json.dump() 保存到 tasks.json；
   - 保存成功返回 True，失败返回 False。
3. 保存参数使用 ensure_ascii=False、indent=4，编码为 UTF-8，
   让 JSON 文件里的中文可直接阅读、格式整齐。

说明：main.py 在 load_tasks() 返回 None 时应结束本次运行，
不能把损坏的数据文件覆盖掉。
"""


def load_tasks():
    # TODO（D）：在这里实现；读取 tasks.json → 返回列表 / [] / None
    pass


def save_tasks(tasks):
    # TODO（D）：在这里实现；写入 tasks.json → 返回 True / False
    pass
