# Dicionarios usam chave e valor para armazenar informações

"""
    variavel = {
        "chave":"valor"
    }
"""


# informacoes do jogador
player = {
    "nome": "Guilherme",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5,
}

# lista de inimigos
npsc = [
    {"nome": "Mostrinho", "dano": 2, "hp": 50, "exp": 5 },
    {"nome": "Monstro", "dano": 5, "hp": 100, "exp": 10},
    {"nome": "Monstrão", "dano": 10, "hp": 150, "exp": 15},
    {"nome": "Chefão", "dano": 25, "hp": 200, "exp": 20},
]

print("O jogador tem o HP", player["hp"])
print("O jogador vai enfrentar o", npsc[1]["nome"], "que tem o HP", npsc[1]["hp"])