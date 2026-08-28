import { describe, it, expect } from "vitest";
import { lucroAcoes } from "./solution";

describe("lucroAcoes", () => {
  it.each([
    [[[7, 1, 5, 3, 6, 4]], 5],
    [[[7, 6, 4, 3, 1]], 0],
    [[[]], 0],
    [[[5]], 0],
    [[[1, 2, 3, 4, 5]], 4],
    [[[3, 3, 3]], 0],
    [[[2, 10]], 8],
    [[[10, 1]], 0],
])("caso", (args: any, esperado: any) => {
    const resultado = lucroAcoes(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
