import { describe, it, expect } from "vitest";
import { aplicarMenu } from "./solution";

describe("aplicarMenu", () => {
  it.each([
    [10, 5, 1, 15],
    [10, 5, 2, 50],
    [10, 5, 3, 10],
    [4, 8, 3, 8],
    [10, 5, 5, null],
    [10, 5, 4, null],
    [10.5, 2.5, 1, 13],
    [-5, -3, 3, -3],
    [7, 7, 3, 7],
    [10, 5, 0, null],
    [10, 5, 6, null],
  ])("f(...) -> %j",
    (valor1, valor2, opcao, esperado) => {
      expect(aplicarMenu(valor1, valor2, opcao)).toEqual(esperado);
    });
  });