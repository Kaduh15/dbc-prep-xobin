import { describe, expect, it } from "vitest";
import { parteInteira } from "./solution";

describe("parteInteira", () => {
  it.each([
    [6.127, 6],
    [100.5, 100],
    [-3.9, -3],
    [7.0, 7],
    [0.999, 0],
  ])("parteInteira(%d) retorna %d", (numero, esperado) => {
    expect(parteInteira(numero)).toBe(esperado);
  });
});