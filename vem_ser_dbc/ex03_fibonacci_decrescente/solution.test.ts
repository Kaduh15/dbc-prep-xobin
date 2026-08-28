import { describe, it, expect } from "vitest";
import { fibonacciDecrescente } from "./solution";

describe("fibonacciDecrescente", () => {
  it.each([
    [[1], [0]],
    [[2], [1, 0]],
    [[3], [2, 1, 0]],
    [[6], [5, 3, 2, 1, 0]],
    [[0], []],
    [[-5], []],
    [[10], [8, 5, 3, 2, 1, 0]],
])("caso", (args: any, esperado: any) => {
    const resultado = fibonacciDecrescente(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
