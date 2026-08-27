import { describe, it, expect } from "vitest";
import { somaDigitos } from "./solution";

describe("somaDigitos", () => {
  it.each([
    [[123], 6],
    [[0], 0],
    [[5], 5],
    [[-123], 6],
    [[999], 27],
    [[1024], 7]
])("caso", (args: any[], esperado: any) => {
    const resultado = somaDigitos(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
