import { describe, expect, it } from "vitest";
import { ordemApresentacao } from "./solution";

describe("ordemApresentacao", () => {
  const alunos = ["Ana", "Bia", "Caio", "Duda"];

  it.each([
    [[1, 3, 0, 2], ["Bia", "Duda", "Ana", "Caio"]],
    [[0, 1, 2, 3], ["Ana", "Bia", "Caio", "Duda"]],
    [[3, 2, 1, 0], ["Duda", "Caio", "Bia", "Ana"]],
  ])("ordemApresentacao(alunos, %j) retorna %j", (indices, esperado) => {
    expect(ordemApresentacao(alunos, indices)).toEqual(esperado);
  });

  it("funciona com um único aluno", () => {
    expect(ordemApresentacao(["Ana"], [0])).toEqual(["Ana"]);
  });
});