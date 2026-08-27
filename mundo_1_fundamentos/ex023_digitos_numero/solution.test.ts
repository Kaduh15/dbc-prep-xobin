import { describe, expect, it } from "vitest";
import { decomporNumero } from "./solution";

describe("decomporNumero", () => {
  it.each([
    [1834, [4, 3, 8, 1]],
    [5, [5, 0, 0, 0]],
    [2764, [4, 6, 7, 2]],
    [0, [0, 0, 0, 0]],
    [100, [0, 0, 1, 0]],
  ])("decomporNumero(%d) retorna %j", (numero, esperado) => {
    expect(decomporNumero(numero)).toEqual(esperado);
  });
});