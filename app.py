from flask import Flask
import utils
import visual

app = Flask(__name__)


@app.route("/")  # Главная страница, выводит список всех кандидатов
def page_index():
    return "<pre>" + utils.candidate_list() + "</pre>"


@app.route("/candidate/<int:x>")  # Выводит кандидата по его Id
def candidates(x):
    candidate = utils.candidate_id(x)
    html_code = visual.visualization_by_pk(candidate)
    return html_code


@app.route("/skills/<x>")  # Выводит список кандидатов по выбранному навыку
def skills(x):
    return "<pre>" + utils.candidate_skill(x) + "</pre>"


if __name__ == "__main__":
    app.run(debug=True)
