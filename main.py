"""程序入口：初始化 QApplication 并显示主窗口。"""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

import config
from ui.main_window import MainWindow


def main() -> int:
    """启动应用，返回进程退出码。"""
    app = QApplication(sys.argv)
    app.setApplicationName(config.APP_NAME)
    app.setApplicationDisplayName(config.APP_DISPLAY_NAME)
    app.setApplicationVersion(config.APP_VERSION)

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
