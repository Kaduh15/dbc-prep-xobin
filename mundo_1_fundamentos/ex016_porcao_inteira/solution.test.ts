import { describe, expect, it } from "vitest";
import { parteInteira } from "./solution";

describe("parteInteira", () => {
  it.each([[6.127, 6],
    [100.5, 100],
    [-3.9, -3],
    [7.0, 7],
    [0.999, 0],
    [-0.5, 0],
    [0.0, 0],
    [-2.0, -2],
    [1.9, 1],
    [123.99, 123],
    [-123.99, -123]])
    ("parteInteira(%d) retorna %d", (numero, esperado) => {
    expect(parteInteira(numero)).toEqual(esperado);
  });
});
