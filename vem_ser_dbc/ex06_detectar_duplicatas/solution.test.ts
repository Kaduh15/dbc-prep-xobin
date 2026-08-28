import { describe, it, expect } from "vitest";
import { detectarDuplicatas } from "./solution";

describe("detectarDuplicatas", () => {
  it.each([
    [[[]], false],
    [[[1]], false],
    [[[1, 2, 3]], false],
    [[[1, 1]], true],
    [[[1, 2, 3, 2]], true],
    [[[0, -1, 0]], true],
])("caso", (args: any, esperado: any) => {
    const resultado = detectarDuplicatas(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
