'''Challenge 73: Crie uma tupla preenchida com os 20 primeiros colocados na tabela do campeonato
brasileiro de futebol, na ordem de colocação. Depois mostre:
- Os 5 primeiros times;
- Os últimos 4 colocados;
- Times em ordem alfabética;
- Em que posição está o time do Fortaleza.'''

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
         'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
         'São Paulo', 'América-MG', 'Botafogo', 'Santos',
         'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')
print(f'Lista de times do Brasileirão: {times}.')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 últimos são: {times[16:20]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O {times[7]} está na 8ª posição!')
