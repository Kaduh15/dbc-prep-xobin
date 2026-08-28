import { describe, it, expect } from "vitest";
import { primeiroUltimoNome } from "./solution";

describe("primeiroUltimoNome", () => {
  it.each([
    [["Jo\u00e3o Silva"], ["Jo\u00e3o", "Silva"]],
    [["Maria Clara Souza"], ["Maria", "Souza"]],
    [["Ana"], ["Ana", "Ana"]],
    [["  Pedro  Henrique  "], ["Pedro", "Henrique"]],
    [[""], ["", ""]],
    [["   "], ["", ""]],
    [["A B C D"], ["A", "D"]],
    [["   Ana   "], ["Ana", "Ana"]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = primeiroUltimoNome(...(args as Parameters<typeof primeiroUltimoNome>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
