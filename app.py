from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Comida con Belén y Chema",
    page_icon="🍽️",
    layout="wide",
)

html = Path("dist/index.html").read_text(encoding="utf-8")
html = html.replace(
    'src="table-background.png"',
    'src="https://gaztelubide-chema-belen.cestola.chatgpt.site/table-background.png"',
)
html = html.replace(
    "<style>",
    "<style>.hero{min-height:760px!important}@media(max-width:760px){.hero{min-height:560px!important}}",
)

components.html(html, height=2500, scrolling=True)
