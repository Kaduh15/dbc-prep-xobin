import { describe, it, expect } from "vitest";
import { maiorEMenor } from "./solution";

describe("maiorEMenor", () => {
  it.each([
    [[3, 7, 5], [7, 3]],
    [[1, 2, 3], [3, 1]],
    [[9, 5, 1], [9, 1]],
    [[-1, -5, -2], [-1, -5]],
    [[9, 9, 9], [9, 9]],
    [[5, 5, 3], [5, 3]],
    [[3, 5, 5], [5, 3]],
    [[5, 3, 5], [5, 3]],
    [[1, 1, 1], [1, 1]],
    [[0, 0, 7], [7, 0]],
    [[7, 5, 7], [7, 5]],
    [[-3, -3, -1], [-1, -3]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = maiorEMenor(...(args as Parameters<typeof maiorEMenor>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
