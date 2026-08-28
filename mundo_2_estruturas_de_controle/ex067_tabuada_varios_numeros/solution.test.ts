import { describe, it, expect } from "vitest";
import { tabuada } from "./solution";

describe("tabuada", () => {
  it.each([
    [[7], [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70]],
    [[5], [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]],
    [[-3], null],
    [[0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    [[12], [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120]],
    [[-1], null],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = tabuada(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
