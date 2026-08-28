import { describe, it, expect } from "vitest";
import { compararNumeros } from "./solution";

describe("compararNumeros", () => {
  it.each([
    [[5, 2], "primeiro maior"],
    [[2, 5], "segundo maior"],
    [[3, 3], "iguais"],
    [[-1, 4], "segundo maior"],
    [[-2, -2], "iguais"],
    [[0, 0], "iguais"],
    [[-3, -7], "primeiro maior"],
    [[5, -10], "primeiro maior"],
    [[0, -1], "primeiro maior"],
    [[-10, -20], "primeiro maior"],
  ] as [number[], string][])("caso %#", (args, esperado) => {
    expect(compararNumeros(args[0], args[1])).toEqual(esperado);
  });
});
