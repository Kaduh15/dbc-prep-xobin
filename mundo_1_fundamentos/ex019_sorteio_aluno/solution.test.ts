import { describe, expect, it } from "vitest";
import { sorteiaAluno } from "./solution";

describe("sorteiaAluno", () => {
  it.each([[["Ana", "Bia", "Caio", "Duda"], 2, "Caio"],
    [["Ana", "Bia", "Caio", "Duda"], 0, "Ana"],
    [["Ana", "Bia", "Caio", "Duda"], 1, "Bia"],
    [["Ana", "Bia", "Caio", "Duda"], 3, "Duda"],
    [["Solo"], 0, "Solo"],
    [["a", "b", "c", "d", "e", "f"], 5, "f"],
    [["a", "b", "c"], 2, "c"]])
    ("sorteiaAluno(%j, %d) retorna %s", (alunos, indice, esperado) => {
    expect(sorteiaAluno(alunos, indice)).toBe(esperado);
  });
});
