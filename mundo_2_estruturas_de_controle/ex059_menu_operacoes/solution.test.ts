import { describe, it, expect } from "vitest";
import { aplicarMenu } from "./solution";

describe("aplicarMenu", () => {
  it.each([
    [10, 5, 1, 15],   // somar
    [10, 5, 2, 50],   // multiplicar
    [10, 5, 3, 10],   // maior
    [4, 8, 3, 8],     // maior
    [10, 5, 5, null], // sair
    [10, 5, 4, null], // novos números
  ])("f(%i, %i, %i) -> %j", (valor1, valor2, opcao, esperado) => {
    expect(aplicarMenu(valor1, valor2, opcao)).toEqual(esperado);
  });
});
