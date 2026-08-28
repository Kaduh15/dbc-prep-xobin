import { describe, it, expect } from "vitest";
import { mediaNotas } from "./solution";


describe('mediaNotas', () => {
  it.each([
    [[7, 7], 7],
    [[5.5, 8.5], 7],
    [[10, 2], 6],
    [[0, 0], 0],
    [[1, 9], 5],
    [[8.5, 7.5], 8],
    [[0, 10], 5],
    [[6.25, 6.25], 6.25],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = mediaNotas(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
