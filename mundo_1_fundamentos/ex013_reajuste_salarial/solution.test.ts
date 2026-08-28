import { describe, expect, it } from "vitest";
import { calculaAumento } from "./solution";

describe("calculaAumento", () => {
  it.each([[1000, 1150.0],
    [2600, 2990.0],
    [0, 0.0],
    [1250, 1437.5],
    [2000, 2300.0],
    [-100, -115.0],
    [1234.56, 1419.744],
    [1, 1.15],
    [10000, 11500.0]])
    ("calculaAumento(%d) retorna %d", (salario, esperado) => {
    expect(calculaAumento(salario)).toBeCloseTo(esperado, 10);
  });
});
