import { describe, expect, it } from "vitest";
import { sorteiaAluno } from "./solution";

describe("sorteiaAluno", () => {
  const alunos = ["Ana", "Bia", "Caio", "Duda"];
  it.each([
    [2, "Caio"],
    [0, "Ana"],
    [1, "Bia"],
    [3, "Duda"],
  ])("sorteiaAluno(alunos, %d) retorna %s", (indice, esperado) => {
    expect(sorteiaAluno(alunos, indice)).toBe(esperado);
  });

  it("funciona com um único aluno", () => {
    expect(sorteiaAluno(["Solo"], 0)).toBe("Solo");
  });
});