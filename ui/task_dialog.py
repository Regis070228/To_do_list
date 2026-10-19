"""任务新增/编辑对话框（组员 A 负责，下一阶段实现）。"""

from __future__ import annotations

from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout


class TaskDialog(QDialog):
    """任务详情对话框占位；当前只显示提示文字。"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("任务")
        self.resize(420, 240)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("任务新增/编辑功能将在后续阶段实现。"))
