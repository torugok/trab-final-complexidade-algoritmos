from metodos_de_busca.buscas import (
    BuscaGulosa,
    BuscaInputDto,
)
from metodos_de_busca.sociedade import Mapa
from metodos_de_busca.metricas import Tempo, Resultado

tempo = Tempo()
mapa = Mapa()
print("Partida: " + mapa.partida.nome)
print("Chegada: " + mapa.chegada.nome)


tempo.inicia_contagem()
resultado = BuscaGulosa().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)
tempo.termina_contagem()

tempo.mostra_tempo(titulo="Busca Gulosa")

Resultado().mostra_resultado(resultado, titulo="Busca Gulosa")

mapa._limpa_busca()

print("---------------------------------")
