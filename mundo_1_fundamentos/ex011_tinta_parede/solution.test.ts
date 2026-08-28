import { describe, it, expect } from "vitest";
import { calcularTinta } from "./solution";


describe('calcularTinta', () => {
  it.each([
    [[2, 2], [4, 2]],
    [[7, 4], [28, 14]],
    [[0, 5], [0, 0]],
    [[2.5, 4], [10, 5]],
    [[3, 3], [9, 4.5]],
    [[4, 2.5], [10, 5]],
    [[0.5, 0.5], [0.25, 0.125]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = calcularTinta(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
