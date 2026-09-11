import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Comida con Belén y Chema",
    page_icon="🍽️",
    layout="wide",
)

html = Path("dist/index.html").read_text(encoding="utf-8")
image = base64.b64encode(Path("dist/table-background.png").read_bytes()).decode()

html = html.replace(
    'src="table-background.png"',
    f'src="data:image/png;base64,{image}"',
)

html = html.replace(
    "<style>",
    "<style>.hero{min-height:760px!important}@media(max-width:760px){.hero{min-height:560px!important}}",
)

components.html(html, height=2500, scrolling=True)
