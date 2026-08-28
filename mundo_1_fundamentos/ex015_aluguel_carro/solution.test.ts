import { describe, expect, it } from "vitest";
import { custoAluguel } from "./solution";

describe("custoAluguel", () => {
  it.each([[8, 720, 588.0],
    [5, 100, 315.0],
    [1, 0, 60.0],
    [0, 0, 0.0],
    [2, 50.5, 127.575],
    [0, 1, 0.15],
    [1, 1, 60.15],
    [3, 0.1, 180.015],
    [10, 1000, 750.0]])
    ("custoAluguel(%d, %d) retorna %d", (dias, km, esperado) => {
    expect(custoAluguel(dias, km)).toBeCloseTo(esperado, 10);
  });
});
