# Team 01 – Усы, лапы и хвост
## Групповой проект по распознаванию лиц
В рамках этого дня вас ждет командный проект, в рамках которого вам предстоит написать модуль для биометрической системы распознавания лиц.

## Оглавление

1. [Глава I](#глава-i) \
    1.1. [Преамбула](#преамбула)
2. [Глава II](#глава-ii) \
    2.1. [Общая инструкция](#общая-инструкция)
3. [Глава III](#глава-iii) \
    3.1. [Цели](#цели)
4. [Глава IV](#глава-iv) \
    4.1. [Задание](#задание)
5. [Глава V](#глава-v) \
    5.1. [Сдача работы и проверка](#сдача-работы-и-проверка)

## Глава I
### Преамбула

Об актуальности и распространенности систем распознавания лиц писать бессмысленно. Они установлены и в телефонах, и на турникетах бизнец-центров, и в метро, и во многих других местах. С точки зрения специалиста по данным, для промышленного внедрения и масштабирования таких систем мало просто подобрать архитектуру нейронки. Нужно еще и описать модель так, чтобы ее можно было встроить в другую информационную систему. Умение писать промышленный код как раз и отличает датасаентиста-студента от датасаентиста-разработчика. Код, полученный от разработчика, должен быть легко понятным и удобно подключаемым в другие модули проекта.

Сегодня вы снова объединитесь в команды и будете писать модуль системы, приближенный к промышленной разработке. На этот раз вы отойдете от исследований в блокноте и должны будете оформить свой код в виде нескольких py-файлов, код из которых импортируется в соседних файлах. Расположение кода в нескольких файлах позволяет его понятно структурировать. Когда ваш коллега впервые увидит такой структурированный код, он сразу будет понимать, что в одном файле написано всё, что связано с базой данных, а в другом - код распознавания лица. Такой подход позволяет вести разработку быстрее и слаженней.

Во время работы над этим проектом вы можете разделить роли в команде по-разному. Например, вы все можете совместно обсуждать и писать код в каждом файле по очереди. Или наоборот: вы можете договориться о том, по каким правилам ваши модули смогут обращаться друг к другу (в этом вам помогут материалы блокнота) и работать над каждым файлом по одиночке, взаимодействуя только на этапе объединения всех файлов в общий проект.

Таким образом, сегодня ваша задача - написать модуль проекта на питоне, который будет распознавать лица. Вы можете использовать любые текстовые редакторы и версии интерпретатора Python, которые вам удобны, но самый простой вариант в рамках технических возможностей нашего курса - вести разработку в блоноте Google Colab и сохранять файлы как `.py`-файлы.


## Глава II
### Общая инструкция

Методология Школы 21 может быть не похожа на тот образовательный опыт, который с вами случался ранее. Ее отличает высокий уровень автономии: у вас есть задача, вы должны ее выполнить. По большей части вам нужно будет самим добывать знания для ее решения. Второй важный момент – это peer-to-peer обучение. В образовательном процессе нет преподавателей и экспертов, перед которыми вы защищаете свой результат. Вы это делаете перед таким же учащимися, как и вы сами. У них есть чек-лист, который поможет им выполнить приемку вашей работы качественно.

Роль Школы 21 заключается в том, чтобы обеспечить через последовательность заданий и оптимальный уровень поддержки такую траекторию обучения, при которой вы освоите не только hard skills, но и научитесь самообучаться.

* Не доверяйте слухам и предположениям о том, как должно быть оформлено ваше решение. Этот документ является единственным источником, к которому стоит обращаться по большинству вопросов.
* Ваше решение будет оцениваться другими учащимися бассейна.
* Подлежат оцениванию только те файлы, которые вы выложили в GIT.
* В вашей папке не должно быть лишних файлов – только те, что были указаны в задании.
* Есть вопрос? Спросите коллегу справа. Не помогло? Спросите коллегу слева.
* Не забывайте, что у вас есть доступ к интернету и поисковым системам.
* Обсуждение заданий можно вести и в Slack бассейна.
* Будьте внимательные к примерам, указанным в этом документе – они могут иметь важные детали, которые не были оговорены другим способом.
* И да пребудет с вами Сила!



## Глава III
### Цели

Наша цель - в рамках командной работы написать модуль распознавания лиц, который можно будет удобно встроить в любой питоновский проект. Кроме того, вы должны понять то, как структурировать код по разным файлам и как в рамках питоновского кода использовать соседние модули.


## Глава IV
### Задание

Сегодня вы будете работать с готовой предобученной нейронкой. Вести разработку на этот раз вы можете в любых доступных средствах. Обратите внимание, что финальный код должен находиться в нескольких py-файлах, а не в ноутбуках, как требовалось во всех предыдущих уроках. Ноутбук с описанием задания этого дня вы сможете найти здесь: `src/t01_task.ipynb`.


Что нужно сделать:
1. Описать проект по архитектуре, указанной в блокноте.
2. Дописать класс Model. Опишите код конструктора и функций `detect_face`, `get_face_embedding`, `compare`, `recognize_from_db`. Внутри этого класса должен использоваться детектор лиц и модель классификации.
3. Дописать класс DataBase. База данных должна хранить данные либо в csv-файле, либо в sqlite на выбор вашей команды. Опишите методы `add_new_face`, `update_face`, `delete_user`, `get`, `get_all`, `count`, `clear`.
4. Описать API вашего модуля в файле api.py. Определите функции, которые реализуют следующий функционал: регистрация нового пользователя (логин + фото или URL фото), обновление данных о пользователе, удаление пользователя, определение пользователя на фотографии, сравнение людей на двух фотографиях (URL фото или само фото), вывод статистики по БД: количество зарегистрированных пользователей, обнуление базы данных.



## Глава V
### Сдача работы и проверка

Вам нужно загрузить в GIT в папку `src` свою папку с файлами с кодом.
1. В папке с кодом должны находиться файлы model.py, database.py, api.py. В папке могут быть дополнительные файлы, если объекты из них используются в перечисленных выше.
2. Папка с кодом должна называться recognition.
