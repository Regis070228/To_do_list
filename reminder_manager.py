"""截止时间与提醒业务逻辑（组员 C 负责）。

本模块只处理普通 Python 字典、列表和时间：
- 不导入 PyQt6，不发送系统通知，不读写文件。
- 是否弹出通知由界面层决定，本模块只返回“现在应该提醒什么”。

统一任务字典示例（与 task_manager.py 完全一致）：
{
    "id": "31594232-239b-4d40-9319-65f4527796f3",
    "title": "完成 Python 作业",
    "description": "提交代码与报告",
    "priority": "高",
    "status": "未完成",
    "due_date": "2026-10-19T23:59:00",
    "reminder_minutes_before": 60,
    "reminder_configured_at": "2026-10-18T15:20:00",
    "reminder_sent_keys": [],
    "created_at": "2026-10-18T15:20:00",
    "updated_at": "2026-10-18T15:20:00",
    "completed_at": None,
}

提醒规则（必须统一）：
1. 每个有截止时间的未完成任务最多两个提醒时刻：
   - 自定义提醒：截止时间减去 reminder_minutes_before（默认 60 分钟）；
   - 固定兜底提醒：截止时间前 30 分钟。
2. 两个时刻相同（例如自定义也是 30 分钟）时只算一个提醒。
3. 提醒标识格式为 "截止时间|提前分钟数"，例如
   "2026-10-19T23:59:00|60"、"2026-10-19T23:59:00|30"。
4. 已完成、无截止时间、全局提醒关闭时不提醒。
5. 截止之后不再补发逾期提醒。
6. 程序重启后可补发“已到提醒时刻但尚未截止”的提醒，
   但要求任务在提醒时刻之前已经存在（比较 reminder_configured_at）。

开发约定：
- 函数签名不要修改，UI 已按这些签名调用。
- 时间统一使用 config.DUE_DATE_FORMAT（YYYY-MM-DDTHH:mm:00）。
- 不需要写测试框架；docstring 里的“典型用例”用于手工验证。
"""

from __future__ import annotations

from datetime import datetime

import config


def validate_due_date(due_date) -> bool:
    """判断截止时间是否合法。

    功能：
        校验界面传入的截止时间字符串。

    参数：
        due_date: None 或 "YYYY-MM-DDTHH:mm:00" 字符串。

    返回：
        合法返回 True，非法返回 False。

    规则与边界：
        - None 表示不设置截止时间，视为合法。
        - 必须能按 config.DUE_DATE_FORMAT 完整解析。
        - 本函数只返回真假，不抛异常，由界面决定如何提示。

    是否修改传入数据：
        不会。

    典型用例：
        - validate_due_date(None)：返回 True。
        - validate_due_date("2026-10-19T23:59:00")：返回 True。
        - validate_due_date("2026-02-30T10:00:00")：返回 False。
        - validate_due_date("10-19 23:59")：返回 False。
    """
    raise NotImplementedError("validate_due_date 由组员 C 实现")


def get_due_level(task, now=None) -> str:
    """返回任务卡片边框的紧迫级别。

    功能：
        根据剩余时间判断卡片边框颜色级别。

    参数：
        task: 任务字典。
        now: 当前时间；None 表示使用系统当前本地时间。

    返回：
        "red" / "yellow" / "white" / "gray"

    规则与边界：
        - 已完成或没有截止时间：返回 "gray"。
        - 已逾期或剩余 ≤ 24 小时：返回 "red"。
        - 剩余 > 24 小时且 ≤ 7 天：返回 "yellow"。
        - 剩余 > 7 天：返回 "white"。
        - 按秒精确比较，不受优先级影响。

    是否修改传入数据：
        不会。

    典型用例：
        - 已完成任务：返回 "gray"。
        - 还剩 2 小时：返回 "red"。
        - 还剩 3 天：返回 "yellow"。
        - 还剩 10 天：返回 "white"。
    """
    raise NotImplementedError("get_due_level 由组员 C 实现")


def format_remaining_time(due_date, now=None) -> str:
    """把剩余时间格式化为中文文本。

    功能：
        生成主界面和提醒弹窗显示的剩余时间。

    参数：
        due_date: "YYYY-MM-DDTHH:mm:00" 或 None。
        now: 当前时间；None 表示使用系统当前本地时间。

    返回：
        中文剩余时间字符串。

    规则与边界：
        - 满一日："2日3时15分"。
        - 不足一日："3时15分"。
        - 不足一时："15分"。
        - 不足一分钟且未逾期："不足1分"。
        - 已逾期："已逾期2日3时15分"，为零的单位可省略。
        - due_date 为 None："未设置"。

    是否修改传入数据：
        不会。

    典型用例：
        - 还剩 2 天 3 小时 15 分：返回 "2日3时15分"。
        - 还剩 3 小时 15 分：返回 "3时15分"。
        - 还剩 15 分：返回 "15分"。
        - 已超过截止 2 小时 15 分：返回 "已逾期2时15分"。
        - due_date 为 None：返回 "未设置"。
    """
    raise NotImplementedError("format_remaining_time 由组员 C 实现")


def get_pending_reminders(tasks, reminders_enabled=True, now=None) -> list:
    """找出当前应当弹出的提醒。

    功能：
        根据自定义提前量和固定 30 分钟兜底规则，返回待提醒项目。

    参数：
        tasks: 任务字典列表。
        reminders_enabled: 全局提醒开关。
        now: 当前时间；None 表示使用系统当前本地时间。

    返回：
        提醒字典列表，每项至少包含：
        {"task_id": ..., "title": ..., "due_date": ..., "reminder_key": ...}

    规则与边界：
        - reminders_enabled 为 False 时直接返回 []。
        - 跳过已完成、没有截止时间、已经发过相同 reminder_key 的任务。
        - 自定义提前量为 30 时，与固定 30 分钟合并，只产生一个提醒键。
        - 已到提醒时刻且尚未截止才返回；截止之后不补发。
        - 重启补发时，要求 reminder_configured_at 不晚于提醒时刻。
        - 本函数不修改任务，也不发送通知。

    是否修改传入数据：
        不会。

    典型用例：
        - 提前 60 分钟的任务，在截止前 60 分钟和 30 分钟各返回一次。
        - 提前 30 分钟的任务，只在截止前 30 分钟返回一次。
        - 提前 5 分钟的任务，先在 30 分钟返回，再在 5 分钟返回。
        - 已完成任务：不返回。
        - reminders_enabled=False：返回 []。
    """
    raise NotImplementedError("get_pending_reminders 由组员 C 实现")


def mark_reminder_sent(task, reminder_key: str) -> None:
    """记录某个提醒已经发出。

    功能：
        把 reminder_key 写入任务的 reminder_sent_keys，避免重复提醒。

    参数：
        task: 任务字典。
        reminder_key: "截止时间|提前分钟数" 格式的提醒标识。

    返回：
        无返回值。

    规则与边界：
        - reminder_key 已存在时不重复追加。
        - 只修改 reminder_sent_keys，不改变 updated_at。
        - 本函数不保存文件，保存由界面调用存储模块完成。

    是否修改传入数据：
        会，直接修改 task["reminder_sent_keys"]。

    典型用例：
        - mark_reminder_sent(task, "2026-10-19T23:59:00|60")：列表新增该键。
        - 再次传入同一个键：列表不重复添加。
    """
    raise NotImplementedError("mark_reminder_sent 由组员 C 实现")
