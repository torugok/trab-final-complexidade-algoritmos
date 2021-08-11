from metodos_de_busca.buscas import (
    BuscaGulosa,
    BuscaInputDto,
)
from metodos_de_busca.sociedade import Mapa


def test_busca_gulosa(snapshot):
    mapa = Mapa()

    resultado = BuscaGulosa().executa(
        BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
    )

    snapshot.assert_match(resultado.exporta(), "busca_gulosa")
