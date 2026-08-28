import { describe, it, expect } from "vitest";
import { somaDigitos } from "./solution";

describe("somaDigitos", () => {
  it.each([
    [[123], 6],
    [[0], 0],
    [[-45], 9],
    [[9], 9],
    [[1000], 1],
    [[7], 7],
])("caso", (args: any[], esperado: any) => {
    const resultado = somaDigitos(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
