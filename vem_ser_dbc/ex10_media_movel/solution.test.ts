import { describe, it, expect } from "vitest";
import { mediaMovel } from "./solution";

describe("mediaMovel", () => {
  it.each([
    [[[1, 2, 3, 4], 2], [1.5, 2.5, 3.5]],
    [[[5], 1], [5.0]],
    [[[1, 2, 3], 3], [2.0]],
    [[[1, 2, 3], 4], []],
    [[[], 2], []],
    [[[1, 2, 3], 0], []],
    [[[1, 2, 3, 4], 3], [2.0, 3.0]],
    [[[-1, -2, -3, -4], 2], [-1.5, -2.5, -3.5]],
])("caso", (args: any, esperado: any) => {
    const resultado = mediaMovel(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
