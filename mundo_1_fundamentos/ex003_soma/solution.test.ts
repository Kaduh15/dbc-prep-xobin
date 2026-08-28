import { describe, it, expect } from "vitest";
import { somar } from "./solution";


describe('somar', () => {
  it.each([
    [[2, 5], 7],
    [[-3, 8], 5],
    [[1.5, 2.5], 4],
    [[0, 0], 0],
    [[-4, -6], -10],
    [[0, 5], 5],
    [[-1.25, 2.75], 1.5],
    [[10, 0], 10],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = somar(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
