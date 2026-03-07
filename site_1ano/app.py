import streamlit as st
from datetime import date
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="Nosso 1 Ano ❤️",
    page_icon="❤️",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

# ---------------- FUNÇÃO FOTO ----------------

def formatar_foto(nome):

    caminho = BASE_DIR / nome
    img = Image.open(caminho)

    largura, altura = img.size
    min_dim = min(largura, altura)

    esquerda = (largura - min_dim) // 2
    topo = (altura - min_dim) // 2
    direita = (largura + min_dim) // 2
    baixo = (altura + min_dim) // 2

    img = img.crop((esquerda, topo, direita, baixo))
    img = img.resize((600,600))

    return img


# ---------------- CSS ----------------

st.markdown("""

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"]{
font-family: 'Poppins', sans-serif;
}

/* FORÇA TEXTO PRETO */

h1,h2,h3,h4,h5,h6,p,span,div,label{
color:black !important;
}

/* FUNDO */

.stApp{
background: linear-gradient(180deg,#fff0f5,#ffe4ec);
}

/* HERO */

.hero{
text-align:center;
padding:60px 20px;
}

.hero-title{
font-size:60px;
color:#ff4b6e !important;
font-weight:600;
}

.hero-sub{
font-size:22px;
}

/* CARD */

.card{
background:white;
padding:30px;
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,0.1);
text-align:center;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
background:#ff4b6e;
}

section[data-testid="stSidebar"] *{
color:white !important;
}

/* BOTÃO */

div.stButton > button{
background-color:#ff4b6e;
color:white;
border-radius:12px;
padding:12px 25px;
font-size:18px;
border:none;
width:100%;
}

div.stButton > button:hover{
background-color:#ff2f57;
}

/* CARTA */

.carta{
background:white;
padding:40px;
border-radius:20px;
box-shadow:0 10px 30px rgba(0,0,0,0.1);
font-size:18px;
line-height:1.7;
}

/* RESPONSIVO */

@media (max-width:768px){

.hero-title{
font-size:40px;
}

.hero-sub{
font-size:18px;
}

.carta{
font-size:16px;
padding:25px;
}

}

/* EU TE AMO */

.amor-overlay{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
display:flex;
align-items:center;
justify-content:center;
pointer-events:none;
animation: fadeOut 3s forwards;
}

.amor-texto{
font-size:90px;
font-weight:700;
color:#ff0000;
animation:pulse 1s infinite alternate;
text-align:center;
}

@keyframes fadeOut{
0%{opacity:1;}
70%{opacity:1;}
100%{opacity:0;}
}

@keyframes pulse{
from{transform:scale(1);}
to{transform:scale(1.1);}
}

</style>

""", unsafe_allow_html=True)


# ---------------- MENU ----------------

pagina = st.sidebar.radio(
"❤️ Menu",
["Início","Memórias","Nossa História","Nossa Música","Quiz","Carta"]
)

# ---------------- INICIO ----------------

if pagina == "Início":

    st.markdown("""
    <div class="hero">
    <div class="hero-title">Cláudio ❤️ Wemilly</div>
    <div class="hero-sub">1 ano de história juntos</div>
    </div>
    """, unsafe_allow_html=True)

    inicio = date(2025,3,9)
    hoje = date.today()

    dias = (hoje - inicio).days

    st.markdown(f"""
    <div class="card">
    <h2>Estamos juntos há</h2>
    <h1 style="font-size:55px;color:#ff4b6e;">{dias} dias ❤️</h1>
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.image(formatar_foto("fotinha1.jpeg"),use_container_width=True)

    with col2:
        st.image(formatar_foto("fotinha2.jpeg"),use_container_width=True)

    with col3:
        st.image(formatar_foto("fotinha3.jpeg"),use_container_width=True)

    if st.button("Clique aqui para uma surpresa ❤️"):
        st.balloons()
        st.success("Eu te amo muito ❤️")

# ---------------- MEMORIAS ----------------

elif pagina == "Memórias":

    st.title("📸 Nossas Memórias")

    col1,col2 = st.columns(2)

    with col1:
        st.image(formatar_foto("fotinha1.jpeg"),caption="Nosso primeiro natal juntos",use_container_width=True)
        st.image(formatar_foto("fotinha2.jpeg"),caption="Primeira vez comendo Sushi-Dog",use_container_width=True)

    with col2:
        st.image(formatar_foto("fotinha3.jpeg"),caption="Minha foto favorita",use_container_width=True)
        st.image(formatar_foto("fotinha4.jpeg"),caption="Piscininha ao seu lado",use_container_width=True)

# ---------------- HISTORIA ----------------

elif pagina == "Nossa História":

    st.title("🗺️ Nossa História")

    st.markdown("""

**💬 Primeiro contato**

O dia em que começamos a conversar e eu percebi o quanto você era especial.

**☕ Primeiro encontro**

Um dos dias mais especiais da minha vida.

**❤️ Pedido de namoro**

O momento em que nossa história começou oficialmente.

**🎉 Nosso primeiro ano**

Um ano cheio de memórias incríveis.

""")

# ---------------- MUSICA ----------------

elif pagina == "Nossa Música":

    st.title("🎵 Nossa Música")

    st.video("https://www.youtube.com/watch?v=450p7goxZqg")

# ---------------- QUIZ ----------------

elif pagina == "Quiz":

    st.title("Quiz sobre nós")

    pontos = 0

    q1 = st.radio("1️⃣ Onde foi nosso primeiro encontro?",["Cinema","Restaurante","Shopping","Alagoa"])
    if q1 == "Shopping":
        pontos +=1

    q2 = st.radio("2️⃣ Qual foi a primeira coisa que fiz ao te ver?",["Nada","Sai Correndo","Te Beijei","Cumprimentei"])
    if q2 == "Te Beijei":
        pontos +=1

    q3 = st.radio("3️⃣ Qual comida mais comemos juntos?",["Lasanha","Sushi","Hambúrguer","Açaí"])
    if q3 == "Açaí":
        pontos +=1

    q4 = st.radio("4️⃣ Onde queremos ver o nascer do Sol?",["Praça","Praia","Casa","Rua"])
    if q4 == "Praia":
        pontos +=1

    q5 = st.radio("5️⃣ Quem manda mais no relacionamento?",["Wemilly","Cláudio","Ninguém","Nós dois"])
    if q5 == "Wemilly":
        pontos +=1

    q6 = st.radio("6️⃣ Quantos anos estamos comemorando agora?",["6 meses","1 ano","2 anos","3 anos"])
    if q6 == "1 ano":
        pontos +=1

    if st.button("Ver resultado ❤️"):

        if pontos >=5:
            st.balloons()
            st.success("Você me conhece muito bem ❤️")

        elif pontos >=3:
            st.info("Acertou algumas 😄")

        else:
            st.error("Errou tudo 😅")

# ---------------- CARTA ----------------

elif pagina == "Carta":

    st.title("💌 Uma carta para você")

    st.markdown("""
    <div class="carta">

Meu amor,

Esse 1 ano ao seu lado foi uma das melhores coisas que já aconteceram na minha vida.

Cada momento com você é especial. Cada risada, cada conversa, cada memória.

Obrigado por fazer parte da minha vida.

Espero viver muitos e muitos anos ao seu lado ❤️

<br><br>

Com todo meu amor<br>
<b>Cláudio</b>

</div>
""", unsafe_allow_html=True)

    if st.button("Clique aqui ❤️"):

        st.balloons()

        st.markdown("""
        <div class="amor-overlay">
        <div class="amor-texto">
        EU TE AMO
        </div>
        </div>
        """, unsafe_allow_html=True)