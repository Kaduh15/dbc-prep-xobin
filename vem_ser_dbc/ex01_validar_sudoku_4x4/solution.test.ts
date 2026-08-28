import { describe, it, expect } from "vitest";
import { validarSudoku4x4 } from "./solution";

describe("validarSudoku4x4", () => {
  it.each([
    [[[[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]], true],
    [[[[1, 1, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]], false],
    [[[[1, 2, 3, 4], [3, 4, 1, 2], [1, 2, 4, 3], [4, 3, 2, 1]]], false],
    [[[[1, 2, 3, 4], [3, 4, 1, 5], [2, 1, 4, 3], [4, 3, 2, 1]]], false],
    [[[[1, 2, 3, 4], [3, 4, 1, 0], [2, 1, 4, 3], [4, 3, 2, 1]]], false],
    [[[[1, 2, 3], [3, 4, 1], [2, 1, 4]]], false],
    [[[]], false],
])("caso", (args: any, esperado: any) => {
    const resultado = validarSudoku4x4(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
