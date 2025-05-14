import streamlit as st
from gemini import gerar_texto, gerar_imagem

# Configuração da página
st.set_page_config(
    page_title="WOLF GENERATOR",
    page_icon="👑👑👑",
    layout="centered",
    initial_sidebar_state="auto",
)

# Estilo customizado
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("https://i.ytimg.com/vi/MYPVQccHhAQ/maxresdefault.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    .main, .block-container {{
        background-color: rgba(255, 255, 255, 0.3);  /* Fundo bem transparente */
        padding: 2rem;
        border-radius: 20px;
    }}
    h1, h2, h3, p, label, .stMarkdown {{
        color: #1a001f;  /* Texto mais escuro para contraste */
        text-shadow: 1px 1px 1px #ffffff88;
    }}
    .stButton > button {{
        background-color: #4B0082;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        border: none;
        transition: 0.3s;
    }}
    .stButton > button:hover {{
        background-color: #370062;
    }}
    .stTextArea, .stTextInput {{
        border-radius: 8px !important;
        background-color: #ffffffaa;
        color: #000;
    }}
    .stRadio > div {{
        background-color: #ffffffaa;
        padding: 10px;
        border-radius: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("# 👑 WOLF GENERATOR")
st.markdown("Gere **textos criativos** ou **imagens realistas** com inteligência artificial.")

# Escolha entre texto ou imagem
modo = st.radio("Escolha o que deseja gerar:", ["Texto", "Imagem"])

# Se for gerar texto
if modo == "Texto":
    tema = st.text_input("📌 Digite um tema para o texto:", placeholder="Ex: Faça uma receita")
    formato = st.selectbox("📝 Escolha o formato do texto:", ["Texto livre", "Artigo", "Poema", "Resumo", "Crônica", "Argumentativo"])
    if st.button("🚀 Gerar Texto"):
        if not tema:
            st.warning("Por favor, insira um tema.")
        else:
            with st.spinner("Gerando texto..."):
                resultado = gerar_texto(tema, formato)
                st.success("✅ Texto gerado com sucesso!")
                st.text_area("📄 Resultado:", resultado, height=300)

# Se for gerar imagem 
else:
    prompt = st.text_input("🎨 Descreva a imagem que deseja gerar:", placeholder="Ex: Estrela grande e luminosa no céu")
    if st.button("🖼️ Gerar Imagem"):
        if not prompt:
            st.warning("Por favor, descreva a imagem.")
        else:
            with st.spinner("Gerando imagem..."):
                resultado_imagem = gerar_imagem(prompt)
                if resultado_imagem.startswith("Ocorreu um erro"):
                    st.error(resultado_imagem)
                else:
                    st.image(resultado_imagem, caption="Imagem Gerada pela IA")
