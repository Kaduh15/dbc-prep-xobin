import { describe, it, expect } from "vitest";
import { tabuada } from "./solution";


describe('tabuada', () => {
  it.each([
    [[7], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]],
    [[2], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],
    [[0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[-3], [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30]],
    [[1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    [[10], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]],
    [[-1], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = tabuada(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
  it("sempre retorna 10 elementos", () => {
    expect(tabuada(5).length).toBe(10);
  });
});
