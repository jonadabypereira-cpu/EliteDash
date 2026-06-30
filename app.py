import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
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

# =========================
# CSS VISUAL
# =========================

st.markdown("""
<style>
.r-box{
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

def get_base64(caminho):
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode()

LOGO_ESQUERDA_B64 = "data:image/png;base64," + get_base64("logo_esquerda.png.png")
LOGO_DIREITA_B64 = "data:image/png;base64," + get_base64("logo_direita.png.png")
