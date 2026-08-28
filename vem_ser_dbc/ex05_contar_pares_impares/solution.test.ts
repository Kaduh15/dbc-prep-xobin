import { describe, it, expect } from "vitest";
import { contarParesImpares } from "./solution";

describe("contarParesImpares", () => {
  it.each([
    [[[]], [0, 0]],
    [[[1]], [0, 1]],
    [[[2]], [1, 0]],
    [[[1, 2, 3, 4]], [2, 2]],
    [[[0]], [1, 0]],
    [[[-2, -3, -4]], [2, 1]],
    [[[2, 4, 6]], [3, 0]],
])("caso", (args: any, esperado: any) => {
    const resultado = contarParesImpares(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
