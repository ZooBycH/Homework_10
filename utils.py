import json

file = open('candidates.json', encoding='utf-8')
data = json.load(file)
file.close()


def candidate_list():
    """Возвращает список все кандидатов с Именем, позицией и навыками"""
    list_page_index = []  # список с данными о кандидатах
    for i in data:
        list_page_index.append(f"<pre>Имя кандидата - {i['name']} \nПозиция кандидата - {i['position']} \n"
                               f"Навыки через запятую - {i['skills']}\n<pre>")
    result = "\n".join(list_page_index)
    return result


def candidate_id(pk):
    """Возвращает данные о кандидате по его id"""
    for i in data:
        if i['id'] == pk:
            pk_str = f"<img src= {i['picture']}>\n<pre>Имя кандидата - {i['name']} " \
                     f"\nПозиция кандидата - {i['position']} \n" \
                     f"Навыки через запятую - {i['skills']}\n<pre>"
            return pk_str


def candidate_skill(skill):
    """Возвращает данные о кандидате по указанному навыку"""
    skill_list = []  # Список с данными о кандидатах с общим навыком
    for i in data:
        check_skills = i['skills'].lower().split(", ")  # список навыков кандидата
        if skill.lower() in check_skills:
            skill_list.append(f"<pre>Имя кандидата - {i['name']} \nПозиция кандидата - {i['position']} \n"
                              f"Навыки через запятую - {i['skills']}\n<pre>")
    result = "\n".join(skill_list)
    return result
