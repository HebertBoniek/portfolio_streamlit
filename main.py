import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Currículo - Hebert Boniek", layout='centered')

dash_faturamento = open("dash_faturamento.mkv", "rb")
dash_faturamento_vd = dash_faturamento.read()

# CSS 
st.markdown("""
    <style>
    /* Fundo da página */
    .stApp {
        background: linear-gradient(135deg, #c1cfde, #5e7485);
        color: black;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Cabeçalhos */
    h1, h2, h3 {
        color: #464f5c;
        font-weight: 600;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #464f5c !important;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Lista */
    ul {
        list-style-type: "✅ ";
        padding-left: 1.2rem;
        color: white; /* Fonte preta também nas listas */
    }
    </style>
""", unsafe_allow_html=True)



def custom_buttom(label, url):
   st.markdown(f"""
    <a href="{url}" target="_blank">
        <div style="background-color: #RRGGBBAA; color: black; padding: 5px; border-radius: 5px; text-align: center;">
            {label}
        </div>
    </a>
    """,
    unsafe_allow_html=True)

translation = {
    "en": {"about_me": "About Me", "projects": "Projects", "contact": "Contact"},
    "pt": {"about_me": "Sobre Mim", "projects": "Projetos", "contact": "Contato"},
}
language = st.sidebar.selectbox("Idioma / Language", ["pt", "en"],
                                format_func=lambda x: "Português" if x == "pt" else "English")
t = translation[language]

st.sidebar.markdown(f"### {t['about_me']}")
section = st.sidebar.radio("", [t["about_me"], t["projects"], t["contact"]])

if section == t["about_me"]:
    st.header(t["about_me"])
    st.write("Tenho experiência com SQL, criando views, realizando queries em banco de dados relacionais, MariaDB e MSSQL."
    " Atuei na criação de Dashboards no PowerBI voltados para o setor comercial, apresentando KPIs e analises objetivando melhorar o desempenho"
    "da equipe de vendas."
    " Desenvolvi Pipelines de extração de dados em Python, afim de automatizar e facilitar a coleta e ingestão de dados para análises posteriores." \
    " Desenvolvi web apps para exibição de dados em tempo real e paineis interativos em Streamlit, fornecendo uma visão rápida das ações diarias das vendas" \
    "Permitindo maior rapidez para a tomada de decisão."
    )

elif section == t["projects"]:
    st.header(t["projects"])
    st.text("Dashboard de Faturamento")
    st.text("Análise de faturamento, criada com dados ficticios. A analise parte de arquivos em xlsx, onde os dados foram tratados, tabelas de faturamento foram unidas" \
    "tabelas fato e dimensão foram relacionadas e as medidas criadas, asssim como as diversas formatações visuais." \
    "Esta análise contempla: ")
    st.markdown(
        """
        - Por Período  
        - Por país e continente  
        - Classificação de produtos em Curva ABC  
        - Análise de Faturamento por loja
        """
    )
    st.video(dash_faturamento_vd)

elif section == t["contact"]:
    st.header(t["contact"])
    
    custom_buttom("Linkedin", "https://linkedin.com/in/hebert-boniek")
    custom_buttom("Celular", "https://wa.me/5531995609255")
    custom_buttom("E-mail", "mailto:hebertboniek56@gmail.com")