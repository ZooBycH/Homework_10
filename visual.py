def visualization_by_pk(i):

    candidates_pk = ""
    candidates_pk += f"<img src=\'{i['picture']}\'>\n"
    candidates_pk += f"{i['name']}\n"
    candidates_pk += f"{i['position']}\n"
    candidates_pk += f"{i['skills']}\n"
    candidates_pk += "\n"

    return "<pre>" + candidates_pk + "</pre>"
