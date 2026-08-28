# Exercício 02 — Prazo de Projeto por Pesos de Dev (Vem Ser DBC / Xobin)

## Descrição do Problema
Dada a equipe (níveis 'junior'|'pleno'|'senior'|'lider' com pesos de produtividade 10/20/30/40 pontos/dia) e os pontos totais do projeto, retorne os dias estimados (pontos ÷ capacidade da equipe). Sem equipe → None.

## Parâmetros e Tipos Esperados
- Assinatura: `def prazo_projeto(equipe: list, pontos: float) -> float | None:`

## Formato do Retorno
- float|None: dias estimados (ou None sem equipe)

## Casos de Exemplo
```python
    ((['junior'], 10), 1.0),
    ((['junior', 'pleno'], 30), 1.0),
    (([], 100), None),
    ((['senior'], 15), 0.5),
```

## Casos de Teste (todos, incluindo extremos)
```python
    ((['junior'], 10), 1.0),
    ((['junior', 'pleno'], 30), 1.0),
    (([], 100), None),
    ((['senior'], 15), 0.5),
    ((['lider'], 80), 2.0),
    ((['junior', 'junior'], 20), 1.0),
    ((['pleno', 'senior'], 25), 0.5),
    ((['junior'], 0), 0.0),
```

## Edge Cases / Extremos
Equipe vazia (→ None); equipe com nível desconhecido (peso 0 → None se zerar); pontos 0 (→ 0); múltiplos do mesmo nível; razões exatas (0.5, 1.0, 2.0).

## Abordagem / Dica
Some os pesos da equipe (capacidade/dia) e divida os pontos por ela. Valide equipe vazia antes de dividir.

## Complexidade
- Tempo O(n), espaço O(1)

## Assinatura Canônica
- **Python**: `def prazo_projeto(equipe: list, pontos: float) -> float | None:`
- **TypeScript**: `export function prazoProjeto(equipe: string[], pontos: number): number | null {`

> Stub para editar: `ex02_prazo_projeto/solution_ex02_prazo_projeto.py` (Python) e `solution.ts` (TS).

