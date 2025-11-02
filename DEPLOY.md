# 🚀 Guia de Deploy - DataGym

## Deploy no GitHub Pages (Mapa HTML)

1. **Inicializar repositório Git:**
```bash
cd DataGymScraper
git init
git add .
git commit -m "Initial commit"
```

2. **Criar repositório no GitHub:**
- Acesse github.com e crie novo repositório "DataGymScraper"
- Não inicialize com README

3. **Push para GitHub:**
```bash
git remote add origin https://github.com/SEU-USUARIO/DataGymScraper.git
git branch -M main
git push -u origin main
```

4. **Ativar GitHub Pages:**
- Settings → Pages → Source: main branch
- O mapa estará em: `https://SEU-USUARIO.github.io/DataGymScraper/gym_map_sao_caetano.html`

## Deploy Streamlit Cloud (App Interativo)

1. **Acesse:** https://streamlit.io/cloud

2. **New app:**
- Repository: `SEU-USUARIO/DataGymScraper`
- Branch: `main`
- Main file: `app.py`

3. **Deploy automático** em ~5 minutos

## Deploy Alternativo - Heroku

1. **Criar Procfile:**
```bash
echo "web: streamlit run app.py --server.port=$PORT" > Procfile
```

2. **Deploy:**
```bash
heroku create datagym-app
git push heroku main
```

## Comandos Úteis

```bash
# Testar localmente
streamlit run app.py

# Atualizar no GitHub
git add .
git commit -m "Update"
git push

# Ver logs Streamlit Cloud
# Acesse dashboard do Streamlit Cloud
```
