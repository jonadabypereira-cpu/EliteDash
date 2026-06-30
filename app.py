import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh
import pytz
import base64
import os

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
# LOGOS (BASE64) - com proteção contra arquivo ausente
# ==================================
def get_base64(caminho):
    """Lê um arquivo de imagem local e retorna em base64.
    Retorna None se o arquivo não existir, em vez de derrubar o app."""
    if not os.path.exists(caminho):
        return None
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Nomes exatamente como estão no repositório GitHub
CAMINHO_LOGO_ESQUERDA = "logo_esquerda.png.png"
CAMINHO_LOGO_DIREITA = "logo_direita.png.png"

logo_esq_data = get_base64(CAMINHO_LOGO_ESQUERDA)
logo_dir_data = get_base64(CAMINHO_LOGO_DIREITA)

LOGO_ESQUERDA_B64 = f"data:image/png;base64,{logo_esq_data}" if logo_esq_data else None
LOGO_DIREITA_B64 = f"data:image/png;base64,{logo_dir_data}" if logo_dir_data else None

# Avisa (sem travar o app) se algum logo não foi encontrado
if logo_esq_data is None:
    st.warning(f"⚠️ Logo não encontrado: {CAMINHO_LOGO_ESQUERDA} (verifique se o arquivo está no repositório, na mesma pasta do app.py)")
if logo_dir_data is None:
    st.warning(f"⚠️ Logo não encontrado: {CAMINHO_LOGO_DIREITA} (verifique se o arquivo está no repositório, na mesma pasta do app.py)")
    
# ==================================
# CABEÇALHO COM LOGOS
# ==================================
# Cria 3 colunas: as laterais para os logos e a central para o texto
st.markdown("""
    <style>
        #cabecalho-compacto {
            padding-top: 0px !important;
            padding-bottom: 0px !important;
        }
        .texto-alinhado {
            text-align: center;
            margin-top: -20px; /* PUXA O TEXTO PARA CIMA, ALINHANDO COM OS LOGOS */
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if LOGO_ESQUERDA_B64:
        st.markdown(f'<img src="{LOGO_ESQUERDA_B64}" width="350">', unsafe_allow_html=True)

with col2:
    # Centraliza o texto vertical e horizontalmente nesta coluna
    st.markdown("""
        <div style="text-align: center;">
           <h3 style="font-size: 30px; margin-bottom: 0;"><i>Provérbios 16:3 "Consagre ao Senhor tudo o que você faz, e os seus planos serão bem-sucedidos."</i><h3>
           <h1 style="font-size: 40px; margin-top: 0; margin-bottom: 0; color: orange;">TIME ELITE</h1>
            <h1 style="font-size: 40px; margin-top: 0; color: green;">🚀 RUMO AOS 180 MILHÕES!</h1>
        </div>
    """, unsafe_allow_html=True)

with col3:
    if LOGO_DIREITA_B64:
        st.markdown(f'<div style="text-align: right;"><img src="{LOGO_DIREITA_B64}"width="180"></div>', unsafe_allow_html=True)

# =========================
# BLOCOS DE LIGAÇÃO
# ========================
horarios = [
    "09:00",
    "10:30",
    "13:45",
    "15:00",
    "16:30"
]

bloco_encontrado = False
for horario in horarios:
    hora_bloco = datetime.strptime(horario, "%H:%M")
    inicio = agora.replace(
        hour=hora_bloco.hour,
        minute=hora_bloco.minute,
        second=0,
        microsecond=0
    )
    fim = inicio + timedelta(minutes=60)
    aviso = inicio - timedelta(minutes=5)

    # BLOCO EM ANDAMENTO
    if inicio <= agora < fim:
        restante = fim - agora
        minutos = int(restante.total_seconds() // 60)
        segundos = int(restante.total_seconds() % 60)
        st.markdown(f"""
        <div class="timer-box ativo">
            <div class="small-text">
                📞 BLOCO DE LIGAÇÃO EM ANDAMENTO
            </div>
            <div class="big-text">
                {minutos:02d}:{segundos:02d}
            </div>
        </div>
        """, unsafe_allow_html=True)
        bloco_encontrado = True
        break

    # FALTAM MENOS DE 5 MINUTOS
    elif aviso <= agora < inicio:
        restante = inicio - agora
        minutos = int(restante.total_seconds() // 60)
        segundos = int(restante.total_seconds() % 60)
        st.markdown(f"""
        <div class="timer-box alerta">
            <div class="small-text">
                ⚠️ BLOCO DE LIGAÇÃO INICIARÁ EM
            </div>
            <div class="big-text">
                {minutos:02d}:{segundos:02d}
            </div>
        </div>
        """, unsafe_allow_html=True)
        bloco_encontrado = True
        break

# FORA DOS BLOCOS
if not bloco_encontrado:
    proximo = None
    for horario in horarios:
        hora_bloco = datetime.strptime(horario, "%H:%M")
        inicio = agora.replace(
            hour=hora_bloco.hour,
            minute=hora_bloco.minute,
            second=0,
            microsecond=0
        )
        if inicio > agora:
            proximo = inicio
            break

    if proximo:
        restante = proximo - agora
        horas = int(restante.total_seconds() // 3600)
        minutos = int((restante.total_seconds() % 3600) // 60)
        st.markdown(f"""
        <div class="timer-box neutro">
            <div class="small-text">
                Próximo bloco de ligação
            </div>
            <div class="big-text">
                {horas}h {minutos}min
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="timer-box neutro">
            <div class="small-text">
                ✅ BLOCOS DO DIA ENCERRADOS.
            </div>
            <div class="big-text">
                Retorno amanhã às 09:00
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==================================
# LEITURA DOS DADOS (GOOGLE SHEETS)
# ==================================
# Planilha pública: aba "faturamento" já contém vendedor, meta, faturado e clientes_novos
GOOGLE_SHEET_ID = "1LL944e77bpkpbDKyOy8-M_N7VKHtlvBTP5UtqAKfxBI"
GOOGLE_SHEET_GID = "0"  # gid da aba "faturamento"
GOOGLE_SHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/{GOOGLE_SHEET_ID}"
    f"/export?format=csv&gid={GOOGLE_SHEET_GID}"
)

try:
    dados = pd.read_csv(GOOGLE_SHEET_URL)
    dados.columns = dados.columns.str.strip()
    dados = dados.dropna(subset=["vendedor"])
    faturamento = dados[["vendedor", "meta", "faturado"]]
    clientes = dados[["vendedor", "clientes_novos"]]
except Exception as e:
    st.error(
        f"❌ Não foi possível carregar os dados da planilha do Google Sheets: {e}. "
        "Verifique se a planilha está compartilhada como 'Qualquer pessoa com o link "
        "pode visualizar' e se a aba 'faturamento' contém as colunas vendedor, meta, "
        "faturado e clientes_novos."
    )
    st.stop()

# ==================================
# CÁLCULOS GERAIS
# ==================================
meta_geral = faturamento["meta"].sum()
faturado_geral = faturamento["faturado"].sum()
percentual = (faturado_geral / meta_geral) * 100
clientes_novos = clientes["clientes_novos"].sum()

# ==================================
# META ESPERADA NO MÊS
# ==================================
dias_uteis_mes = 21
dias_uteis_passados = 19  # ajuste diariamente
percentual_esperado = (dias_uteis_passados / dias_uteis_mes) * 100

# ==================================
# TÍTULO
# ==================================
st.markdown("""
<div style="
height:40px;
">
</div>
""", unsafe_allow_html=True)

# ==================================
# RESUMO GERAL
# ==================================
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Meta Geral", f"R$ {meta_geral:,.0f}")
col2.metric("Faturado", f"R$ {faturado_geral:,.0f}")
col3.metric("% Atingido", f"{percentual:.1f}%")
col4.metric("Clientes Novos", int(clientes_novos))
col5.metric("% Esperado", f"{percentual_esperado:.1f}%")

st.markdown("<hr style='margin:1px;'>", unsafe_allow_html=True)

# ==================================
# PERFORMANCE INDIVIDUAL
# ==================================
ranking = faturamento.sort_values(by="faturado", ascending=False)
resultado = pd.merge(ranking, clientes, on="vendedor", how="left")

st.subheader("👤 Performance Individual")

dias_uteis_mes = 21
dias_uteis_passados = 19
cards_por_linha = 7

for i in range(0, len(resultado), cards_por_linha):
    cols = st.columns(cards_por_linha)
    for j in range(cards_por_linha):
        if i + j < len(resultado):
            vendedor = resultado.iloc[i + j]
            meta = vendedor["meta"]
            faturado = vendedor["faturado"]
            clientes_novos_vendedor = vendedor["clientes_novos"]
            percentual_meta = (faturado / meta)
            percentual_esperado = (dias_uteis_passados / dias_uteis_mes)

            if percentual_meta >= 1:
                cor = "#2e871e"
            elif percentual_meta >= 0.85:
                cor = "#2299f7"
            elif percentual_meta >= percentual_esperado:
                cor = "#ac7e11"
            else:
                cor = "#b62828"

            with cols[j]:
                st.markdown(
                    f"""
                    <div style="
                    background:{cor};
                    padding:10px;
                    border-radius:10px;
                    text-align:center;
                    min-height:1px;
                    border:0px solid rgba(55,55,55,0.02);
                    box-shadow:0 0px 0px rgba(0,0,0,0.15);
                    ">
                    <div style="
                    color:white;
                    font-size:22px;
                    font-weight:900;
                    text-align:center;
                    width:100%;
                    margin:0 auto 8px auto;
                    display:block;
                    ">
                    {"🏆 " + vendedor['vendedor'] if i + j == 0 else vendedor['vendedor']}
                    </div>
                    <div style="margin-top:5px;">
                    META
                    </div>
                    <div style="
                    color:white;
                    font-size:20px;
                    font-weight:bold;
                    ">
                    R$ {meta:,.0f}
                    </div>
                    <div style="margin-top:5px;">
                    FATURADO
                    </div>
                    <div style="
                    color:white;
                    font-size:20px;
                    font-weight:bold;
                    ">
                    R$ {faturado:,.0f}
                    </div>
                    <div style="margin-top:5px;">
                    CLIENTES NOVOS
                    </div>
                    <div style="
                    color:white;
                    font-size:20px;
                    font-weight:bold;
                    ">
                    {clientes_novos_vendedor}
                    </div>
                    <div style="
                    margin-top:5px;
                    color:white;
                    font-size:16px;
                    font-weight:600;
                    ">
                    {percentual_meta*100:.1f}% da meta
                    </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

st.markdown("""
<div style="height:30px;"></div>
""", unsafe_allow_html=True)

st.subheader("🎯 Faixas de Performance")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="
        background:#2e871e;
        color:white;
        padding:2px;
        border-radius:10px;
        text-align:center;
        font-size:14px;
        font-weight:bold;">
        🟢 VERDE<br>
        Meta Batida
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background:#2299f7;
        color:white;
        padding:2px;
        border-radius:10px;
        text-align:center;
        font-size:14px;
        font-weight:bold;">
        🔵 AZUL<br>
        Acima de 85% da meta
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background:#D4AF37;
        color:white;
        padding:2px;
        border-radius:10px;
        text-align:center;
        font-size:14px;
        font-weight:bold;">
        🟡 DOURADO<br>
        Acima do percentual esperado
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
        background:#b62828;
        color:white;
        padding:2px;
        border-radius:10px;
        text-align:center;
        font-size:14px;
        font-weight:bold;">
        🔴 VERMELHO<br>
        Abaixo do percentual esperado
    </div>
    """, unsafe_allow_html=True)
