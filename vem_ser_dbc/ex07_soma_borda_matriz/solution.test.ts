import { describe, it, expect } from "vitest";
import { somaBordaMatriz } from "./solution";

describe("somaBordaMatriz", () => {
  it.each([
    [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], 40],
    [[[[5]]], 5],
    [[[[1, 2], [3, 4]]], 10],
    [[[]], 0],
    [[[[]]], 0],
    [[[[1, 2, 3, 4]]], 10],
    [[[[-1, -2], [-3, -4]]], -10],
])("caso", (args: any, esperado: any) => {
    const resultado = somaBordaMatriz(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
