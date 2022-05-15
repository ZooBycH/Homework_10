from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")  # Главная страница, выводит список всех кандидатов
def page_index():
    return f"{utils.candidate_list()}"


@app.route("/candidate/<int:x>")  # Выводит кандидата по его Id
def candidates(x):
    return f" {utils.candidate_id(x)}"


@app.route("/skills/<x>")  # Выводит список кандидатов по выбранному навыку
def skills(x):
    return f" {utils.candidate_skill(x)}"


if __name__ == "__main__":
    app.run(debug=True)
