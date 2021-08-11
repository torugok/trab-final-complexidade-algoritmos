from metodos_de_busca.sociedade.cidade import Vizinho
from typing import List

from metodos_de_busca.sociedade import Cidade

from .busca import IBusca, BuscaInputDto, ResultadoBusca


class BuscaGulosa(IBusca):
    def __init__(self):
        self.arvore_de_busca: List[Vizinho] = []
        self.caminho: List[Vizinho] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        input_dto.partida.visitar()

        # Se chegou na "chegada" finaliza o algoritmo
        if input_dto.partida.nome == input_dto.chegada.nome:
            return ResultadoBusca(
                caminho=self.caminho, arvore_de_cidades=self.arvore_de_busca
            )
        # Caso Contrário
        else:
            # Verifica se o primeiro vizinho foi visitado
            if input_dto.partida.vizinhos[0].cidade_destino.foi_visitado():
                # Se sim, Visita o segundo vizinho
                cidade_a_visitar = input_dto.partida.vizinhos[1]
            else:
                # Caso contrário, visita o primeiro vizinho
                cidade_a_visitar = input_dto.partida.vizinhos[0]

            # Vai em cada vizinho procurando por cidades que não foram visitadas
            for vizinho in input_dto.partida.vizinhos:
                # Se esse vizinho nao foi visitado
                if not vizinho.cidade_destino.foi_visitado():
                    custo = vizinho.cidade_destino.heuristica
                    custo_a_visitar = cidade_a_visitar.cidade_destino.heuristica
                    # Se o custo da cidade que foi escolhida para ser visitada for menor
                    # que o custo da heuristica do vizinho, então define a cidade a visitar como sendo o vizinho
                    if custo < custo_a_visitar:
                        cidade_a_visitar = vizinho

            # Adiciona a arvore e ao caminho
            self.arvore_de_busca.append(cidade_a_visitar)
            self.caminho.append(cidade_a_visitar)

            # Usa de recursão para executar o algoritmo múltiplas vezes
            return self.executa(
                BuscaInputDto(
                    partida=cidade_a_visitar.cidade_destino,
                    chegada=input_dto.chegada,
                )
            )
