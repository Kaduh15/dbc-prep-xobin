import { describe, it, expect } from "vitest";
import { maiorMenor } from "./solution";

describe("maiorMenor", () => {
  it.each([
    [[[3, 1, 4, 1, 5]], [5, 1]],
    [[[]], null],
    [[[7]], [7, 7]],
    [[[-1, -5, -3]], [-1, -5]],
    [[[0, 0]], [0, 0]],
    [[[100, 5, 200]], [200, 5]],
])("caso", (args: any[], esperado: any) => {
    const resultado = maiorMenor(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
