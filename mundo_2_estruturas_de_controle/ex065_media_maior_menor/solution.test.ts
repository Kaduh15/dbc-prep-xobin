import { describe, it, expect } from "vitest";
import { estatisticas } from "./solution";

describe("estatisticas", () => {
  it.each([
    [[[7, 5, 8, 3]], [5.75, 8, 3]],
    [[[10]], [10.0, 10, 10]],
    [[[2, 9, 4]], [5.0, 9, 2]],
    [[[5, 5, 5, 5]], [5.0, 5, 5]],
    [[[-5, 0, 5]], [0.0, 5, -5]],
    [[[7, 7, 7]], [7.0, 7, 7]],
    [[[3]], [3.0, 3, 3]],
    [[[]], [0.0, 0, 0]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = estatisticas(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
