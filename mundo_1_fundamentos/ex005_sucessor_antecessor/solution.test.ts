import { describe, it, expect } from "vitest";
import { sucessorAntecessor } from "./solution";


describe('sucessorAntecessor', () => {
  it.each([
    [[10], [9, 11]],
    [[0], [-1, 1]],
    [[-5], [-6, -4]],
    [[1], [0, 2]],
    [[2], [1, 3]],
    [[-1], [-2, 0]],
    [[100], [99, 101]],
    [[-100], [-101, -99]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = sucessorAntecessor(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
