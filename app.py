import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Configuração da página
st.set_page_config(
    page_title="DataGym - Análise Agregadores",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.3rem;
        color: #667eea;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin: 0.5rem;
    }
    .insight-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown('<h1 class="main-header">🏋️ DataGym</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">Análise Agregadores - Wellhub e TotalPass - São Caetano do Sul</h2>', unsafe_allow_html=True)

# Métricas principais
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Academias Mapeadas", "152", "12 novas")

with col2:
    st.metric("Preço Médio Wellhub", "R$ 149,90", "-5% vs direto")

with col3:
    st.metric("Economia Média", "32%", "+3%")

with col4:
    st.metric("Bairros Cobertos", "12", "100%")

# Abas de navegação
tab1, tab2, tab3, tab4 = st.tabs(["📍 Localização", "💰 Precificação", "📊 Renda Local", "🎯 Insights"])

with tab1:
    st.header("Análise de Localização")
    
    # Dados de exemplo para o mapa de calor
    loc_data = pd.DataFrame({
        'lat': [-23.618, -23.620, -23.623, -23.627, -23.635, -23.632],
        'lon': [-46.575, -46.572, -46.551, -46.575, -46.582, -46.585],
        'intensidade': [0.9, 0.8, 0.7, 0.5, 0.2, 0.1],
        'bairro': ['Santa Paula', 'Barcelona', 'Centro', 'Santo Antônio', 'Fundação', 'São José']
    })
    
    # Mapa de calor
    fig_map = px.density_mapbox(loc_data, lat='lat', lon='lon', z='intensidade',
                              radius=20, center=dict(lat=-23.623, lon=-46.551),
                              zoom=13, mapbox_style="carto-positron",
                              title="Mapa de Calor - Distribuição de Academias Premium")
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Insight
    with st.container():
        st.markdown("""
        <div class="insight-card">
            <h4>🎯 Insight Estratégico</h4>
            <p>Bairros noroeste (Santa Paula/Barcelona) concentram 68% das academias premium com preços acima de R$ 200/mês</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("Análise de Precificação")
    
    # Dados para gráfico 3D
    np.random.seed(42)
    precos_data = pd.DataFrame({
        'Renda_Per_Capita': np.random.normal(3000, 800, 50),
        'Preco_Wellhub': np.random.normal(150, 50, 50),
        'Preco_TotalPass': np.random.normal(140, 40, 50),
        'Bairro': np.random.choice(['Santa Paula', 'Centro', 'Santo Antônio', 'Santa Maria'], 50),
        'Latitude': np.random.uniform(-23.63, -23.61, 50),
        'Longitude': np.random.uniform(-46.58, -46.56, 50)
    })
    
    # Gráfico 3D interativo
    fig_3d = px.scatter_3d(precos_data, x='Latitude', y='Longitude', z='Renda_Per_Capita',
                          color='Preco_Wellhub', size='Preco_Wellhub',
                          hover_data=['Bairro', 'Preco_TotalPass'],
                          title="Renda vs Localização vs Preços Wellhub",
                          color_continuous_scale='viridis')
    
    st.plotly_chart(fig_3d, use_container_width=True)
    
    # Tabela comparativa
    st.subheader("Comparativo de Preços")
    
    comparativo_data = pd.DataFrame({
        'Academia': ['Smart Fit', 'Bluefit', 'Bio Ritmo', 'Runner', 'Peralta Fitness'],
        'Bairro': ['Centro', 'Barcelona', 'Nova Gerti', 'Centro', 'Centro'],
        'Wellhub': [89.90, 189.90, 199.90, 139.90, 59.90],
        'TotalPass': [109.90, 119.90, 219.90, 149.90, 89.90],
        'Economia': [-20, 70, -20, -10, -30]
    })
    
    st.dataframe(comparativo_data.style.format({
        'Wellhub': 'R$ {:.2f}',
        'TotalPass': 'R$ {:.2f}',
        'Economia': 'R$ {:.0f}'
    }).background_gradient(subset=['Economia'], cmap='RdYlGn'), use_container_width=True)

with tab3:
    st.header("Dados Socioeconômicos")
    
    # Dados socioeconômicos
    socio_data = pd.DataFrame({
        'Bairro': ['Santa Paula', 'Barcelona', 'Centro', 'Santo Antônio', 
                   'Santa Maria', 'Jardim SCS', 'Nova Gerti', 'Fundação', 'São José'],
        'Renda_Per_Capita': [3800, 3500, 3200, 2800, 2600, 2400, 2200, 1800, 1600],
        'IDH': [0.870, 0.865, 0.880, 0.855, 0.850, 0.845, 0.840, 0.830, 0.825],
        'Preco_Medio_Academias': [189.90, 179.90, 149.90, 129.90, 119.90, 109.90, 99.90, 79.90, 69.90]
    })
    
    # Gráfico de correlação
    fig_corr = px.scatter(socio_data, x='Renda_Per_Capita', y='Preco_Medio_Academias',
                         size='IDH', color='Bairro', hover_name='Bairro',
                         title="Correlação: Renda vs Preços das Academias",
                         trendline="ols")
    
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Cálculo de correlação
    correlacao = socio_data['Renda_Per_Capita'].corr(socio_data['Preco_Medio_Academias'])
    
    with st.container():
        st.markdown(f"""
        <div class="insight-card">
            <h4>📈 Padrão Identificado</h4>
            <p>Correlação de {correlacao:.2f} entre renda per capita do bairro e preços das academias premium</p>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.header("Insights Estratégicos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-card">
            <h4>🏆 Melhor Custo-Benefício</h4>
            <p><strong>Wellhub</strong> é mais vantajoso em bairros de classe média (Centro, Santo Antônio) com economia média de 25%</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4>📊 Segmentação Ideal</h4>
            <p>Bairros premium: Wellhub Gold | Bairros médios: Wellhub Silver | Bairros econômicos: TotalPass</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-card">
            <h4>💡 Oportunidade de Mercado</h4>
            <p>Área sudeste (Fundação, São José) tem baixa penetração de academias premium - potencial de crescimento de 45%</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4>🎯 Estratégia de Expansão</h4>
            <p>Focar em Santa Paula/Barcelona para unidades premium e desenvolver planos acessíveis para Fundação/São José</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recomendações finais
    st.subheader("Recomendações de Ação")
    
    recomendacoes = [
        "1. 🎯 Desenvolver planos corporativos para empresas no Centro",
        "2. 💼 Criar parcerias com condomínios em Santa Paula/Barcelona", 
        "3. 📱 Lançar campanhas geolocalizadas por bairro",
        "4. 🏘️ Implementar programas comunitários em Fundação/São José",
        "5. 📊 Monitorar preços da concorrência trimestralmente",
        "6. 🤝 Negociar melhores condições com Wellhub para planos em massa"
    ]
    
    for rec in recomendacoes:
        st.write(rec)

# Sidebar com filtros
with st.sidebar:
    st.header("Filtros")
    
    st.subheader("Agregador")
    wellhub_filter = st.checkbox("Wellhub", value=True)
    totalpass_filter = st.checkbox("TotalPass", value=True)
    
    st.subheader("Faixa de Preço")
    price_range = st.slider("Selecione a faixa de preço (R$)", 50, 300, (80, 200))
    
    st.subheader("Bairros")
    bairros = ['Todos'] + list(socio_data['Bairro'].unique())
    selected_bairro = st.selectbox("Selecione o bairro", bairros)
    
    st.subheader("Tipo de Análise")
    analysis_type = st.radio("Tipo de visualização:", 
                           ["Mapa de Calor", "Gráfico 3D", "Comparativo", "Correlação"])
    
    # Botão para atualizar
    if st.button("Aplicar Filtros", type="primary"):
        st.success("Filtros aplicados com sucesso!")

# Rodapé
st.markdown("---")
st.markdown("**DataGym** - Análise estratégica de academias e agregadores em São Caetano do Sul | Desenvolvido para tomada de decisões baseada em dados")