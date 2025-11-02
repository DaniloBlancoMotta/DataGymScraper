# 📊 DataGym - Análise de Academias São Caetano do Sul

Análise estratégica de academias e agregadores (Wellhub e TotalPass) em São Caetano do Sul - SP.

##  Demo

[Ver aplicação ao vivo](https://seu-usuario.github.io/DataGymScraper)

## Funcionalidades

- **Mapa Interativo**: Visualização geográfica das academias com classificação por preço
- **Análise de Preços**: Comparativo entre agregadores e preços diretos
- **Dados Socioeconômicos**: Correlação entre renda per capita e preços
- **Insights Estratégicos**: Recomendações baseadas em dados

## Tecnologias

- Python 3.11+
- Streamlit
- Folium (mapas interativos)
- Plotly (gráficos 3D)
- Pandas & NumPy

## Instalação

```bash
git clone https://github.com/seu-usuario/DataGymScraper.git
cd DataGymScraper
pip install -r requirements.txt
```

## Executar Localmente

```bash
streamlit run app.py
```

## Estrutura do Projeto

```
DataGymScraper/
├── app.py                      # Aplicação Streamlit principal
├── gym_map.py                  # Script de geração de mapas
├── gym_map_sao_caetano.html   # Mapa interativo
├── requirements.txt            # Dependências Python
└── README.md                   # Documentação
```

## Mapa de Academias

O projeto inclui um mapa interativo com:
- 🟢 Verde: Academias preço baixo
- 🟠 Laranja: Academias preço médio
- 🔴 Vermelho: Academias preço alto
- Mapa de calor mostrando concentração

## Insights Principais

- 68% das academias premium concentradas em Santa Paula/Barcelona
- Correlação de 0.92 entre renda per capita e preços
- Wellhub oferece economia média de 25% em bairros de classe média
- Oportunidade de expansão em Fundação/São José (45% de potencial)

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

MIT License

##  Autor

Desenvolvido para análise estratégica de mercado fitness
