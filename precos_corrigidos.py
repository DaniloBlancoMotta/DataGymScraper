precos_wellhub = {
    'Academia Runner São Caetano': 139.90, 'Peralta Fitness': 59.90, 
    'Academia Bio Ritmo': 199.90, 'Ironberg São Caetano': 399.90,
    'Bluefit': 189.90, 'Sport & Fit': 99.90, 'Evoque Academia Av. Goiás': 89.90,
    'F2 Fitness': 139.90, 'Academia RRFIT': 59.90, 'Energy Academia': 89.90,
    'Academia Inova São Caetano': 289.90, 'Smart Fit - Fundação': 89.90,
    'Smart Fit - Santa Paula': 89.90, 'Guerrero Gym': 129.90, 'Academia Magnum': 109.90,
    'Cross São Caetano': 199.90, 'Sfida Fitness': 289.90, 'Academia AGilis': 99.90,
    'Academia Eizens Sport Center': 119.90, 'Academia Max Power': 99.90,
    'Academia Poliesportiva Triathlon': 89.90, 'Academia Up Life': 109.90,
    'Academia Delphos': 89.90, 'Fit Balance': 129.90, 'Max Power Modelagem Física': 99.90,
    'Miani Fitness Academia': 99.90, 'Scherk Academia': 99.90, 'Sprint Academia': 109.90,
    'Evoque Academia - Unidade Alameda': 89.90, 'Espaço Cerâmica Crossfit': 179.90
}

precos_totalpass = {
    'Academia Runner São Caetano': 149.90, 'Peralta Fitness': 89.90,
    'Academia Bio Ritmo': 219.90, 'Ironberg São Caetano': 399.90,
    'Bluefit': 119.90, 'Sport & Fit': 109.90, 'Evoque Academia Av. Goiás': 99.90,
    'F2 Fitness': 149.90, 'Academia RRFIT': 79.90, 'Energy Academia': 99.90,
    'Academia Inova São Caetano': 269.90, 'Smart Fit - Fundação': 109.90,
    'Smart Fit - Santa Paula': 109.90, 'Guerrero Gym': 139.90, 'Academia Magnum': 119.90,
    'Cross São Caetano': 189.90, 'Sfida Fitness': 279.90, 'Academia AGilis': 109.90,
    'Academia Eizens Sport Center': 129.90, 'Academia Max Power': 109.90,
    'Academia Poliesportiva Triathlon': 99.90, 'Academia Up Life': 119.90,
    'Academia Delphos': 99.90, 'Fit Balance': 139.90, 'Max Power Modelagem Física': 109.90,
    'Miani Fitness Academia': 109.90, 'Scherk Academia': 109.90, 'Sprint Academia': 119.90,
    'Evoque Academia - Unidade Alameda': 99.90, 'Espaço Cerâmica Crossfit': 169.90
}

df['preco_wellhub'] = df['nome'].map(precos_wellhub)
df['preco_totalpass'] = df['nome'].map(precos_totalpass)
df['gap_preco'] = df['preco_wellhub'] - df['preco_totalpass']
