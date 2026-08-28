import { describe, expect, it } from "vitest";
import { analisarNome } from "./solution";

describe("analisarNome", () => {
  it.each([["Maria Silva", ["MARIA SILVA", "maria silva", 10, 5]],
    ["JOAO PEREIRA", ["JOAO PEREIRA", "joao pereira", 11, 4]],
    ["A", ["A", "a", 1, 1]],
    ["Ana Clara de Souza", ["ANA CLARA DE SOUZA", "ana clara de souza", 15, 3]],
    ["Joao", ["JOAO", "joao", 4, 4]],
    ["LUIZ CARLOS", ["LUIZ CARLOS", "luiz carlos", 10, 4]],
    ["Ana  Paula", ["ANA  PAULA", "ana  paula", 8, 3]]])
    ("analisarNome(%s) retorna %j", (nome, esperado) => {
    expect(analisarNome(nome)).toEqual(esperado);
  });
});
