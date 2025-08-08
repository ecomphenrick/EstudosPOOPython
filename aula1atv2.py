import random
from models.armas import Espada, Arma, Cajado
from models.entidades import Guerreiro, Mago

# Simulação do combate
def combate(entidade1, entidade2):
    print("\n--- COMBATE INICIADO ---\n")
    turno = 1

    while entidade1.esta_vivo() and entidade2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        if turno % 2 == 1:
            entidade1.atacar(entidade2)
        else:
            entidade2.atacar(entidade1)
        turno += 1

    print("\n--- FIM DO COMBATE ---")
    if entidade1.esta_vivo():
        print(f"\n🏆 {entidade1.nome} venceu com {entidade1.vida} de vida restante!")
    else:
        print(f"\n🏆 {entidade2.nome} venceu com {entidade2.vida} de vida restante!")


# ===== EXECUÇÃO PRINCIPAL =====

if __name__ == "__main__":
    guerreiro = Guerreiro("Arthas", vida=100, forca=25)
    mago = Mago("Gandalf", vida=90, inteligencia=35)

    espada = Espada(dano_base=20, comprimento=100)
    cajado = Cajado(dano_base=18, elemento="fogo")

    # TODO: Criar método equipar_arma e modificar método atacar para se adequar à arma equipada.
    # guerreiro.equipar_arma(espada)
    # mago.equipar_arma(cajado)

    combate(guerreiro, mago)