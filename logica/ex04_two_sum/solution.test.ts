import { describe, it, expect } from "vitest";
import { twoSum } from "./solution";

describe("twoSum", () => {
  it.each([
    [[[2, 7, 11, 15], 9], [0, 1]],
    [[[3, 2, 4], 6], [1, 2]],
    [[[3, 3], 6], [0, 1]],
    [[[], 5], null],
    [[[1, 2, 3], 99], null],
    [[[-1, -2, -3], -3], [0, 1]],
    [[[0, 0, 1], 0], [0, 1]],
    [[[5, 5, 5], 10], [0, 1]],
    [[[1], 1], null],
])("caso", (args: any[], esperado: any) => {
    const resultado = twoSum(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
