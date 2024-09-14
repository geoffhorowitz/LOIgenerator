# for style elements to import into streamlit app

# system imports
import streamlit as st

def load_css():
    return """
    <style>
    .center-logo {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%; /* Adjust height as needed */
    }
    .center-text {
        text-align: center;
    }
    .left-text {
        text-align: left;
    }
    .center-button {
        display: flex;
        justify-content: center;
    }
    .default-button {
        background-color: #008000, 
        color: white
    }
    </style>
    """

def logo_html():
    return '<div class="center-logo"><img src="../assets/GG_logo.png" width="150"/></div>'

def title_html(title):
    return f'<h1 class="left-text">{title}</h1>'

def subtitle_html(subtitle):
    return f'<h2 class="center-text">{subtitle}</h2>'