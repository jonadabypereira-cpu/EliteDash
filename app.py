import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh
import pytz
import base64

# =========================
# CONFIGURAÇÃO
# =========================

st.set_page_config(
    page_title="Painel Elite",
    layout="wide"
)
st.markdown("""
<style>
/* Remove espaços do Streamlit */
.block-container{
    padding-top:0rem;
    padding-bottom:0rem;
    padding-left:0.5rem;
    padding-right:0.5rem;
}

header{
visibility:hidden;
}
footer{
visibility:hidden;
}

/* remove espaço acima */
div[data-testid="stVerticalBlock"]{
gap:0.0rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stMetricValue"]{
    color:white;
    font-size:28px;
    font-weight:bold;
}
[data-testid="stMetricLabel"]{
    color:#5497e7 !important;
}
[data-testid="stMetricLabel"] p{
    font-size:18px !important;
    font-weight:400 !important;
    color:white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
[data-testid="stMetric"] {
    background-color: #1C1F26;
    padding:7px;
    border-radius:15px;
}
h1 {
    color:white;
    font-size:20px !important;
}
h2 {
    color:white;
    font-size:20px !important;
}
h3 {
    color:white;
    font-size:22px !important;
}
</style>
""", unsafe_allow_html=True)

# Atualiza a tela a cada segundo
st_autorefresh(interval=1000, key="timer")

# =========================
# CSS VISUAL
# =========================

st.markdown("""
<style>
.timer-box{
padding:6px;
border-radius:15px;
text-align:center;
margin-bottom:5px;
font-weight:bold;
}
.alerta{
    background-color:#ff4b4b;
    color:white;
}
.ativo{
    background-color:#00b050;
    color:white;
}
.neutro{
    background-color:#1f2937;
    color:white;
}
.big-text{
    font-size:42px;
}
.small-text{
    font-size:24px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HORÁRIO BRASÍLIA
# =========================

tz = pytz.timezone("America/Sao_Paulo")
agora = datetime.now(tz)

# ==================================
# IMAGENS EMBUTIDAS (BASE64)
# ==================================

# Logo Godi Transportes (Esquerda)
LOGO_ESQUERDA_B64 = "data:image/png;base64,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"

# Logo Team Elite (Direita)
LOGO_DIREITA_B64 = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/2wBDAQICAgICAgUDAwUKBwYHCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgr/wAARCAKAA8ADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usld3dx5cp63x8fH19fZ3uHi4uPd3yvPj4+MwMHCw0TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8vZ0fODR4uPk5ebn6Onq8
