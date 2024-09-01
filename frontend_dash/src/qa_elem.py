
from dash import Dash, dcc, html, Input, Output, no_update, State

def qa_elem(question_text: str, id_text: str) -> list:
    return [
        dcc.Markdown(f"### {question_text}"),
        dcc.Input(
            id=f"{id_text}",
            value="",
            className="w-100",
            placeholder=f"{question_text}",
        ),
    ]


    