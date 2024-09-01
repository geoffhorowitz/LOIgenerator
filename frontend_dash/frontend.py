
# system imports
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

# local imports
from frontend_css import SIDEBAR_STYLE, CONTENT_STYLE
from src.form import Form
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

sidebar = html.Div(
        [
            html.H4("Generosity Genius"),
            html.Hr(),
            html.P(
                "LOI Generator", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Your Organization", href="/org", active="exact"),
                    dbc.NavLink("Target Foundation", href="/foundation", active="exact"),
                    dbc.NavLink("Your Project", href="/project", active="exact"),
                    dbc.NavLink("Additional Info", href="/additional", active="exact"),
                    dbc.NavLink("Generate LOI", href="/generate", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/org":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/foundation":
        foundation_form = Form('foundation_questions', 'Target Foundation Information')
        return foundation_form.get_form()
    elif pathname == "/project":
        return html.P("Oh cool, this is page 2!")
    elif pathname == "/additional":
        return html.P("Oh cool, this is page 2!")
    elif pathname == "/generate":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)