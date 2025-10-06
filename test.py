#реестр гномиков
import sys
from pathlib import Path
import sqlite3
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, \
    QGridLayout, QLineEdit, QSpinBox, QSlider, QLabel, QPushButton, \
    QListWidget

class Gnomiki(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Реестр гномиков")
        self.conn = sqlite3.connect("gnomiki.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS gnomiki (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, height INTEGER)")
        self.cur.execute("SELECT name,height FROM gnomiki")
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("Имя"),0,0)
        layout.addWidget(QLabel("Рост"),1,0)
        self.name_entry = QLineEdit()
        layout.addWidget(self.name_entry,0,1)
        self.height_entry = QSlider(Qt.Orientation.Horizontal)
        self.height_entry.setTickPosition(
            QSlider.TickPosition.TicksBelow
        )
        self.height_entry.setRange(1, 10)
        self.height_entry.setSingleStep(1)
        self.height_entry.setPageStep(1)
        layout.addWidget(self.height_entry,1,1)
        self.btn = QPushButton("Добавить")
        self.btn.clicked.connect(self.add_gnome)
        layout.addWidget(self.btn,2,0,1,2)
        self.gnome_lst = QListWidget()
        layout.addWidget(self.gnome_lst,3,0,1,2)
        self.get_all_gnomes()
        self.show()

    def add_gnome(self):
        if self.name_entry.text().strip():
            sql = "insert into gnomiki(name, height) values(?,?)"
            self.cur.execute(sql,(self.name_entry.text().strip(), self.height_entry.value()))
            self.conn.commit()
            self.get_all_gnomes()

    def get_all_gnomes(self):
        self.gnome_lst.clear()
        self.cur.execute('select name,height from gnomiki')
        ans = self.cur.fetchall()
        print(ans)
        if ans:
            for item in ans:
                self.gnome_lst.addItem(f"{item[0]} - {item[1]}см.")



app = QApplication(sys.argv)
app.setStyleSheet(Path('style.qss').read_text())
window = Gnomiki()
sys.exit(app.exec())