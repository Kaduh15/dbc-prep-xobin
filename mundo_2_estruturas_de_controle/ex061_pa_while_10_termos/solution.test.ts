import { describe, it, expect } from "vitest";
import { dezTermosPa } from "./solution";

describe("dezTermosPa", () => {
  it.each([
    [[2, 3], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]],
    [[1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    [[10, -2], [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]],
    [[5, 0], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],
    [[0, 4], [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]],
    [[-3, -1], [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12]],
    [[7, 2], [7, 9, 11, 13, 15, 17, 19, 21, 23, 25]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = dezTermosPa(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
