
# system imports
from dash import Dash, dcc, html, Input, Output, no_update, State
import dash_bootstrap_components as dbc

# local imports
from .qa_elem import qa_elem

def get_n_questions(ref_field) -> int:
    # TODO
    return 1
    
def get_questions_list(ref_field) -> list:
    # TODO
    return ['I am a question']

class Form:
    def __init__(self, ref_field, header_text) -> None:
        self.form = None
        self.ref_field = ref_field
        self.header_text = header_text
        self.n_questions = get_n_questions(ref_field)
        self.questions_list = get_questions_list(ref_field)
        self.generate_form()

    def generate_form(self):
        content = []
        
        # Header
        content.append(html.H4(f"{self.header_text}", className="text-center"))

        #dbc.Row([
        #        dbc.Col(
        #            qa_elem('q1', 'q1')
        #            width=6,
        #        ),
        #        dbc.Col(
        #            qa_elem('q2', 'q2')
        #            width=6, 
        #     ),]),
        
        # Questions
        for ndx in range(self.n_questions):
            content.append(
                dbc.Row(qa_elem(self.questions_list[ndx], f'{self.ref_field}-{ndx}'))
            )

        # Footer
        content.extend(
            [
                html.Br(),
                dbc.Row(
                    [
                        dbc.Button(
                            "Move to next section", id="submit-button", color="primary"
                        )
                    ]
                ),
                dbc.Modal(
                    id="modal",
                    size="lg",
                ),
                dcc.Markdown(
                    """Learn more about Generosity Genius on our [website](https://www.generositygenius.org)!""",
                    link_target="_blank",
                    className="mt-4 text-center",
                ),
            ]
        )

        # put in container and set form object
        self.form = dbc.Container(content, fluid = True)

    def get_form(self):
        return self.form
