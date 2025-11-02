import pandas as pd
import folium
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

# Gym data
gyms = [
    {"name": "Academia Runner São Caetano", "address": "Rua Maranhão, 1050, Centro, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Peralta Fitness", "address": "Rua Santa Catarina, 40, Centro, São Caetano do Sul, SP", "price": "High"},
    {"name": "Academia Bio Ritmo", "address": "Rua Visconde de Inhaúma, 308, Nova Gerti, São Caetano do Sul, SP", "price": "High"},
    {"name": "Ironberg", "address": "Rua Maj. Carlos Del Prete, 1725, Santo Antônio, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Bluefit", "address": "Rua Alegre, 1289, Barcelona, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Sport & Fit", "address": "Av. Pres. Kennedy, 2000, Santa Maria, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Evoque Academia Av. Goiás", "address": "Av. Goiás, 1631, Santa Paula, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "F2 Fitness", "address": "Av. Pres. Kennedy, 1407, Santa Paula, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Academia RRFIT", "address": "Rua Oswaldo Cruz, 249, Santa Paula, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Energy Academia", "address": "Rua Visc. de Inhaúma, 387, Oswaldo Cruz, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Academia Inova São Caetano", "address": "Av. Goiás, 1040, Santa Paula, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Smart Fit - Fundação", "address": "Rua Aquidaban, Fundação, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Smart Fit - Santa Paula", "address": "Santa Paula, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Guerrero Gym", "address": "Av. Sen. Roberto Símonsen, 855, Santo Antônio, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Academia Magnum", "address": "Rua Nelly Pellegrino, 888, Nova Gerti, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Cross São Caetano", "address": "São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Sfida Fitness", "address": "Santa Paula, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Academia AGilis", "address": "Rua Oswaldo Cruz, 669, Santa Paula, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Academia Eizens Sport Center", "address": "Rua Maceió, 489, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Academia Max Power", "address": "Rua Baraldi, 814, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Academia Poliesportiva Triathlon", "address": "Rua Visconde Inhaúma, 308, São Caetano do Sul, SP", "price": "High"},
    {"name": "Academia Up Life", "address": "Rua Ceará, 393, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Academia Delphos", "address": "Rua Senador Flaquer, 145, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Fit Balance", "address": "Avenida Goiás, 172, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Max Power Modelagem Física", "address": "Rua Baraldi, 814, Centro, São Caetano do Sul, SP", "price": "Low"},
    {"name": "Miani Fitness Academia", "address": "Rua Francesco de Martini, 549, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Scherk Academia", "address": "Rua Piauí, 919, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Sprint Academia", "address": "Avenida Senador Roberto Simonsen, 855, Santo Antônio, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Evoque Academia - Unidade Alameda", "address": "Rua Arlíndo Marcheti, 338, Santa Maria, São Caetano do Sul, SP", "price": "Medium"},
    {"name": "Espaço Cerâmica Crossfit", "address": "Rua Primeiro de Maio, 20, São José, São Caetano do Sul, SP", "price": "Medium"},
]

df_gyms = pd.DataFrame(gyms)

# Geocode addresses
geolocator = Nominatim(user_agent="gym_mapper")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def get_coordinates(address):
    try:
        location = geocode(address)
        if location:
            return location.latitude, location.longitude
    except:
        pass
    return None, None

print("Geocoding addresses...")
df_gyms[['latitude', 'longitude']] = df_gyms['address'].apply(
    lambda x: pd.Series(get_coordinates(x))
)

# Create map centered on São Caetano do Sul
gym_map = folium.Map(location=[-23.6237, -46.5547], zoom_start=14)

# Price colors
price_color = {'Low': 'green', 'Medium': 'orange', 'High': 'red'}

# Add circle markers
for idx, row in df_gyms.iterrows():
    if pd.notna(row['latitude']) and pd.notna(row['longitude']):
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=8,
            popup=f"<b>{row['name']}</b><br>Preço: {row['price']}",
            color=price_color[row['price']],
            fill=True,
            fillColor=price_color[row['price']],
            fillOpacity=0.7,
            weight=2
        ).add_to(gym_map)

# Add heatmap
heat_data = [[row['latitude'], row['longitude']] 
             for idx, row in df_gyms.iterrows() 
             if pd.notna(row['latitude']) and pd.notna(row['longitude'])]
HeatMap(heat_data, radius=15, blur=25, max_zoom=13).add_to(gym_map)

# Save map
gym_map.save('gym_map_sao_caetano.html')
print(f"\nMapa salvo como 'gym_map_sao_caetano.html'")
print(f"Academias geocodificadas: {df_gyms['latitude'].notna().sum()}/{len(df_gyms)}")
