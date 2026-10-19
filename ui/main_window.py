"""主窗口（组员 A / 项目负责人负责）。

当前只提供能够启动的最简窗口，用于验证项目框架。
本阶段不调用 task_manager、reminder_manager、storage 中的未实现函数。
"""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget

import config


class MainWindow(QMainWindow):
    """应用主窗口；后续在这里接入三视图和任务卡片。"""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(config.APP_DISPLAY_NAME)
        self.resize(960, 640)

        central = QWidget(self)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(24, 24, 24, 24)

        title = QLabel(config.APP_DISPLAY_NAME)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: 600;")

        hint = QLabel("项目框架已就绪，业务功能将在后续阶段接入。")
        hint.setAlignment(Qt.AlignmentFlag.AlignCenter)

        version = QLabel(f"版本 {config.APP_VERSION}")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version.setStyleSheet("color: #666666;")

        layout.addStretch(1)
        layout.addWidget(title)
        layout.addWidget(hint)
        layout.addWidget(version)
        layout.addStretch(1)
        self.setCentralWidget(central)
