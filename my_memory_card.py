
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QGroupBox, QButtonGroup
from random import shuffle, randint



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600,300)


RadioGroupBox = QGroupBox('Варианты ответов')
question = QLabel('Какой национальности не существует?')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Чулымцы')
btn_answer3 = QRadioButton('Смурфы')
btn_answer4 = QRadioButton('Алеуты')
btn = QPushButton('Ответить')


class Qwestion():
    def __init__(self, qwestion, right_answer, wrong1, wrong2, wrong3):
        self.right_answer = right_answer
        self.question = qwestion
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def show_question():
    btn.setText('Ответить')
    ans_GroupBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)    
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    btn.setText('Следующий вопрос')
    ans_GroupBox.show()
    RadioGroupBox.hide()



answers=[btn_answer1, btn_answer2, btn_answer3, btn_answer4]


def ask(q: Qwestion):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2) 
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    answer2.setText(q.right_answer)
    show_question()



def click_OK():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_qustion()
    

def next_qustion():
    main_win.total += 1
    print('Статистика \n-Всего вопросов:' + str(main_win.total)+'\n-Правильных ответов:' + str(main_win.score))
    cur_qustion = randint(0, len(qustions_list) -1)
    q = qustions_list[cur_qustion]
    ask(q)


def show_correct(res):
    answer1.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика \n-Всего вопросов:' + str(main_win.total)+'\n-Правильных ответов:' + str(main_win.score))
        print('Рейтинг:', (main_win.score/main_win.total * 100))
    else:

        show_correct('Неправильно')
        print('Неверно')
        print('Рейтинг:', (main_win.score/main_win.total * 100))


layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()


layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)


layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)


layout_main = QVBoxLayout()


layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
RadioGroupBox.setLayout(layout_main)


ans_GroupBox = QGroupBox()
answer1 = QLabel('Правильно/Неправильно')
answer2 = QLabel('Правильный ответ')


vl = QVBoxLayout()
vl.addWidget(answer1)
vl.addWidget(answer2)
ans_GroupBox.setLayout(vl)
ans_GroupBox.hide()


layout= QVBoxLayout()
layout.addWidget(question)
layout.addWidget(RadioGroupBox)
layout.addWidget(ans_GroupBox)
layout.addWidget(btn)
main_win.setLayout(layout)


RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)


qustions_list = []


q = Qwestion('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Русский', 'Украинский')
qustions_list.append(q)


q1 = Qwestion('Почему новый год зимой?', 'Так решил Дед Мороз', 'Потому что', 'Не знаю', 'Это всё Снегурочка')
qustions_list.append(q1)


q2 = Qwestion('Что такое Машина?', 'Машина', 'Металл и железо', 'Куча железа', 'Металл на колёсах')
qustions_list.append(q2)













main_win.score = 0
main_win.total = 0

btn.clicked.connect(click_OK)
next_qustion()



main_win.show()
app.exec_()
