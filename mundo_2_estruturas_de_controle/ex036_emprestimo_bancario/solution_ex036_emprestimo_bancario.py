def prestacao_mensal(valor_casa: float, anos: int) -> float:
    """Prestacao mensal = valor_casa / (anos * 12)."""
    raise NotImplementedError


def aprova_emprestimo(valor_casa: float, salario: float, anos: int) -> bool:
    """True se prestacao <= 30% do salario."""
    raise NotImplementedError
