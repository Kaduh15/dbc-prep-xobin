import { describe, it, expect } from "vitest";
import { dobroTriploRaiz } from "./solution";


describe('dobroTriploRaiz', () => {
  it.each([
    [[9], [18, 27, 3]],
    [[4], [8, 12, 2]],
    [[0], [0, 0, 0]],
    [[2], [4, 6, 1.4142135623730951]],
    [[7], [14, 21, 2.6457513110645907]],
    [[16], [32, 48, 4]],
    [[1], [2, 3, 1]],
    [[0.5], [1, 1.5, 0.7071067811865476]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = dobroTriploRaiz(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
