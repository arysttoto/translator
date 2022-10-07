from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from googletrans import Translator
app = QApplication([])
window = QWidget()
window.setWindowTitle('Translator')
# window.resize(300, 300)
vl = QVBoxLayout()
translator = Translator()

h1 = QHBoxLayout()
russian = QLabel('Russian')
english = QLabel('English')
h1.addWidget(russian)
h1.addWidget(english)

h2 = QHBoxLayout()
russian_box = QTextEdit()
english_box = QTextEdit()
h2.addWidget(russian_box)
h2.addWidget(english_box)

h3 = QHBoxLayout()
trans_btn = QPushButton('Translate!')
h3.addWidget(trans_btn)


vl.addLayout(h1)
vl.addLayout(h2)
vl.addLayout(h3)

def set_to_eng():
    russian_text = russian_box.toPlainText()
    new_eng = translator.translate(russian_text, dest='en')
    english_box.setText(new_eng.text)

trans_btn.clicked.connect(set_to_eng)


window.setLayout(vl)
window.show()
app.exec()
