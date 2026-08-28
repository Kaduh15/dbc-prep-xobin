import { describe, it, expect } from "vitest";
import { somaIgnorandoFlag } from "./solution";

describe("somaIgnorandoFlag", () => {
  it.each([
    [[[2, 5, 999]], [2, 7]],
    [[[1, 2, 3, 999]], [3, 6]],
    [[[999]], [0, 0]],
    [[[]], [0, 0]],
    [[[1, 999, 2]], [2, 3]],
    [[[999, 1, 999, 2, 999]], [2, 3]],
    [[[-5, 999, 10]], [2, 5]],
    [[[1, 2, 3]], [3, 6]],
    [[[999, 999]], [0, 0]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = somaIgnorandoFlag(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
