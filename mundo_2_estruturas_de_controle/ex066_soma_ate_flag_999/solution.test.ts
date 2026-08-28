import { describe, it, expect } from "vitest";
import { numerosAte999 } from "./solution";

describe("numerosAte999", () => {
  it.each([
    [[[5, 999]], [1, 5]],
    [[[7, 8, 999, 10]], [2, 15]],
    [[[999]], [0, 0]],
    [[[]], [0, 0]],
    [[[1, 999]], [1, 1]],
    [[[1, 2, 999, 4, 999]], [2, 3]],
    [[[1, 2, 3]], [3, 6]],
    [[[999, 10]], [0, 0]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = numerosAte999(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
