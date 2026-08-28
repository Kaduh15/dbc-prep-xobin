import { describe, it, expect } from "vitest";
import { parOuImpar } from "./solution";

describe("parOuImpar", () => {
  it.each([
    [[4, 2, 'par'], true],
    [[5, 4, 'impar'], true],
    [[4, 2, 'impar'], false],
    [[3, 4, 'par'], false],
    [[7, 3, 'par'], true],
    [[7, 3, 'PAR'], true],
    [[5, 5, 'impar'], false],
    [[0, 0, 'par'], true],
    [[1, 2, 'impar'], true],
    [[2, 4, 'impar'], false],
    [[3, 4, 'IMPAR'], true],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = parOuImpar(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
