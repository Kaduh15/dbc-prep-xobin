import { describe, it, expect } from "vitest";
import { maiorMenor } from "./solution";

describe("maiorMenor", () => {
  it.each([
    [[[3, 1, 4, 1, 5]], [5, 1]],
    [[[-1, 2, -3]], [2, -3]],
    [[[7]], [7, 7]],
    [[[]], null],
    [[[10, 10]], [10, 10]]
])("caso", (args: any[], esperado: any) => {
    const resultado = maiorMenor(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
