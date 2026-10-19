"""Windows 系统集成（组员 D / 项目负责人负责）。

本模块只处理当前用户的开机自启项：
- 使用 Windows 注册表 HKEY_CURRENT_USER 下的 Run 项。
- 不需要管理员权限，不影响其他软件的自启项。
- 不导入 PyQt6，不读写任务集。
"""

from __future__ import annotations


def get_autostart_state() -> bool:
    """查询本程序是否已加入开机自启。

    返回：
        注册表中存在本程序自启项时返回 True，否则返回 False。

    规则与边界：
        - 只检查本程序专属的注册表项名称。
        - 读取失败时返回 False，由界面提示实际状态。
    """
    raise NotImplementedError("get_autostart_state 由 D 实现")


def set_autostart(enabled: bool, executable_path: str) -> None:
    """开启或关闭当前用户的开机自启。

    参数：
        enabled: True 表示开启，False 表示关闭。
        executable_path: 已安装程序的 EXE 绝对路径。

    返回：
        无返回值。

    规则与边界：
        - 只写入或删除本程序自己的自启项。
        - 写入路径需要加引号，避免空格导致启动失败。
        - 未打包的源码环境可抛出 RuntimeError，提示仅安装版支持。
        - 注册表操作失败时抛出异常，由界面提示。
    """
    raise NotImplementedError("set_autostart 由 D 实现")
