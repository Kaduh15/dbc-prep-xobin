from typing import Tuple


def analisar_pessoas(pessoas: list[Tuple[str, int, str]]) -> Tuple[float, str, int]:
    """Analisa dados de um grupo de pessoas (ex.: 4 pessoas).

    Args:
        pessoas (list[Tuple[str, int, str]]): lista de registros (nome, idade, sexo),
            onde sexo é 'M' (masculino) ou 'F' (feminino).

    Returns:
        Tuple[float, str, int]: (média de idade do grupo, nome do homem mais velho,
        quantidade de mulheres com menos de 20 anos). Se não houver homem, o nome
        é uma string vazia.
    """
    raise NotImplementedError
