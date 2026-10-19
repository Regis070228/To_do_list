"""全局配置：版本号、便携版数据路径和公共常量。

本文件只负责计算路径和定义常量，不创建目录、不读写文件。
所有路径都是绝对路径；业务代码不要自己写 "./" 或 "../" 相对路径。

便携版数据位置：
- 源码运行：项目根目录（config.py 所在目录）
- 打包运行：EXE 所在目录（sys.executable 的父目录）
settings.json 与 user_data/ 都放在该目录下。
"""

from __future__ import annotations

import sys
from pathlib import Path

# ---------- 应用与版本 ----------
APP_NAME = "ToDoList"
APP_DISPLAY_NAME = "To-do List 待办清单"
APP_VERSION = "0.1.0"
DATA_SCHEMA_VERSION = 2

# ---------- 路径 ----------
_IS_FROZEN = getattr(sys, "frozen", False)

# 资源文件：打包后位于 PyInstaller 解包目录；源码运行时为项目根目录。
if _IS_FROZEN and hasattr(sys, "_MEIPASS"):
    RESOURCE_DIR = Path(sys._MEIPASS)
else:
    RESOURCE_DIR = Path(__file__).resolve().parent

# 用户数据：便携版与 EXE 同级；源码运行时为项目根目录。
# 不要把可写数据放到 sys._MEIPASS，那是打包后的临时目录。
if _IS_FROZEN:
    APP_DIR = Path(sys.executable).resolve().parent
else:
    APP_DIR = Path(__file__).resolve().parent

DATA_DIR = APP_DIR
USER_DATA_DIR = DATA_DIR / "user_data"
SETTINGS_FILE = DATA_DIR / "settings.json"

# ---------- 业务常量 ----------
PRIORITY_HIGH = "高"
PRIORITY_MEDIUM = "中"
PRIORITY_LOW = "低"
PRIORITIES = (PRIORITY_HIGH, PRIORITY_MEDIUM, PRIORITY_LOW)
DEFAULT_PRIORITY = PRIORITY_MEDIUM

STATUS_PENDING = "未完成"
STATUS_COMPLETED = "已完成"
STATUSES = (STATUS_PENDING, STATUS_COMPLETED)

VIEW_DUE_DATE = "due_date"
VIEW_PRIORITY = "priority"
VIEW_COMPLETED = "completed"
VIEW_MODES = (VIEW_DUE_DATE, VIEW_PRIORITY, VIEW_COMPLETED)
DEFAULT_VIEW = VIEW_DUE_DATE

DEFAULT_TASKSET_NAME = "我的任务"
DEFAULT_REMINDER_MINUTES = 60      # 用户未设置时的自定义提醒提前量
FALLBACK_REMINDER_MINUTES = 30     # 固定兜底提醒
REMINDER_MINUTES_MIN = 0
REMINDER_MINUTES_MAX = 10080

# ---------- 时间格式 ----------
DUE_DATE_FORMAT = "%Y-%m-%dT%H:%M:00"
DISPLAY_DUE_FORMAT = "%m-%d %H:%M"
DISPLAY_FULL_FORMAT = "%Y-%m-%d %H:%M"

# ---------- 设置默认值 ----------
DEFAULT_SETTINGS = {
    "active_taskset_id": "",
    "reminders_enabled": True,
    "autostart_enabled": False,
    "close_to_tray": True,
    "close_prompt_shown": False,
}

# ---------- 统一数据格式 ----------
# 任务字典（任务集 JSON 中 tasks 列表的元素）必须包含以下字段：
# {
#     "id": "31594232-239b-4d40-9319-65f4527796f3",
#     "title": "完成 Python 作业",
#     "description": "提交代码与报告",
#     "priority": "高",
#     "status": "未完成",
#     "due_date": "2026-10-19T23:59:00",
#     "reminder_minutes_before": 60,
#     "reminder_configured_at": "2026-10-18T15:20:00",
#     "reminder_sent_keys": [],
#     "created_at": "2026-10-18T15:20:00",
#     "updated_at": "2026-10-18T15:20:00",
#     "completed_at": null,
# }
TASK_FIELDS = (
    "id",
    "title",
    "description",
    "priority",
    "status",
    "due_date",
    "reminder_minutes_before",
    "reminder_configured_at",
    "reminder_sent_keys",
    "created_at",
    "updated_at",
    "completed_at",
)

# 任务集 JSON 的顶层结构：
# {
#     "schema_version": 2,
#     "taskset_id": "<uuid>",
#     "taskset_name": "学习任务",
#     "tasks": [任务字典, ...]
# }
TASKSET_FIELDS = ("schema_version", "taskset_id", "taskset_name", "tasks")
