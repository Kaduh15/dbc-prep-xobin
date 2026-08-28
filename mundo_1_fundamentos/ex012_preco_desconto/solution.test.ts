import { describe, it, expect } from "vitest";
import { precoComDesconto } from "./solution";


describe('precoComDesconto', () => {
  it.each([
    [[100, 0.05], 95],
    [[80, 0.05], 76],
    [[100, 0.1], 90],
    [[0, 0.05], 0],
    [[100], 95],
    [[200, 0.05], 190],
    [[50, 0.1], 45],
    [[100, 0], 100],
    [[1, 1], 0],
    [[1, 0.5], 0.5],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = precoComDesconto(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
