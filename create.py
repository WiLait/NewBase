import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import os  # Заменяем pathlib

# Укажите путь к вашему файлу UI
ui_path = "C:/Users/User/Documents/PyQt6/login_form.ui"

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Загружаем UI напрямую, без класса
    window = uic.loadUi(ui_path)
    window.show()

    sys.exit(app.exec())