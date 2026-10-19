"""任务集与设置的本地存储（组员 D / 项目负责人负责）。

本模块只做文件读写：
- 不导入 PyQt6，不写界面逻辑，不处理任务排序或提醒判断。
- 所有路径都来自 config.py，禁止在业务代码里手写相对路径。

运行时的用户数据目录（由本模块按需创建）：
    %LOCALAPPDATA%/ToDoList/
    ├── settings.json
    └── user_data/
        ├── <taskset_uuid_1>.json
        └── <taskset_uuid_2>.json

单个任务集 JSON 的结构（schema_version=2）：
{
    "schema_version": 2,
    "taskset_id": "93d659c3-b640-4fc9-9273-b5e50c118f73",
    "taskset_name": "学习任务",
    "tasks": [
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
            "completed_at": None
        }
    ]
}

开发约定：
- 任务集文件名使用 UUID，显示名称保存在 taskset_name 中。
- 读取到损坏或版本不兼容的文件时抛出明确异常，不能当成空数据覆盖。
- 保存时先写同目录临时文件，再替换目标文件。
- 本阶段只保留接口；实现由 D 在下一阶段完成。
"""

from __future__ import annotations


def list_tasksets() -> list:
    """列出 user_data 目录中的所有任务集。

    返回：
        任务集摘要列表，每项至少包含 id 和 name，
        例如 [{"id": "...", "name": "我的任务"}, ...]。

    规则与边界：
        - 目录不存在时返回空列表，不创建目录。
        - 跳过损坏或版本不兼容的文件，并在界面提示。
    """
    raise NotImplementedError("list_tasksets 由 D 实现")


def create_taskset(name: str) -> dict:
    """新建一个空任务集并保存为独立 JSON 文件。

    参数：
        name: 任务集显示名称，去掉首尾空白后不能为空，不能与现有名称重复。

    返回：
        新任务集字典（schema_version、taskset_id、taskset_name、tasks）。

    规则与边界：
        - 文件名使用新的 UUID，不使用用户输入的名称。
        - 名称为空或重复时抛出 ValueError。
        - 创建后不自动切换活动任务集。
    """
    raise NotImplementedError("create_taskset 由 D 实现")


def load_taskset(taskset_id: str) -> dict:
    """读取指定任务集。

    参数：
        taskset_id: 任务集 UUID。

    返回：
        任务集字典。

    规则与边界：
        - 文件不存在抛 FileNotFoundError。
        - JSON 损坏、字段缺失或 schema_version 不是 2 时抛出明确异常。
        - 只读取，不修改设置中的活动任务集。
    """
    raise NotImplementedError("load_taskset 由 D 实现")


def save_taskset(taskset: dict) -> None:
    """保存一个任务集。

    参数：
        taskset: 完整任务集字典。

    返回：
        无返回值。

    规则与边界：
        - 保存前做基本字段校验。
        - 使用临时文件写入后替换，失败时保留原文件。
        - 写入 UTF-8 JSON，保留中文。
    """
    raise NotImplementedError("save_taskset 由 D 实现")


def import_taskset(file_path: str, display_name: str | None = None) -> dict:
    """从外部 JSON 导入一个任务集副本。

    参数：
        file_path: 外部任务集 JSON 的绝对路径。
        display_name: 可选的新名称；None 表示沿用文件中的名称。

    返回：
        已保存到 user_data 的新任务集字典。

    规则与边界：
        - 一次只导入一个任务集，不合并到现有任务集。
        - 必须符合当前 schema_version=2。
        - 导入副本分配新的 taskset_id，保留任务 ID 和内容。
        - 名称与现有任务集重复时抛出 ValueError，要求重新命名。
    """
    raise NotImplementedError("import_taskset 由 D 实现")


def export_taskset(taskset_id: str, file_path: str) -> None:
    """把指定任务集导出为 JSON 文件。

    参数：
        taskset_id: 要导出的任务集 UUID。
        file_path: 用户选择的导出路径。

    返回：
        无返回值。

    规则与边界：
        - 导出保留原 taskset_id 和全部任务字段。
        - 写入失败时抛出异常，由界面提示。
    """
    raise NotImplementedError("export_taskset 由 D 实现")


def load_settings() -> dict:
    """读取全局设置。

    返回：
        设置字典；缺失的已知字段用 config.DEFAULT_SETTINGS 补齐。

    规则与边界：
        - settings.json 不存在时返回默认设置。
        - 文件损坏时抛出明确异常，不能静默当成首次运行。
        - 保留未知但合法的扩展键。
    """
    raise NotImplementedError("load_settings 由 D 实现")


def save_settings(settings: dict) -> None:
    """保存全局设置。

    参数：
        settings: 设置字典。

    返回：
        无返回值。

    规则与边界：
        - 只写入已识别的设置和未知扩展键。
        - 使用临时文件替换，失败时保留原文件。
    """
    raise NotImplementedError("save_settings 由 D 实现")
