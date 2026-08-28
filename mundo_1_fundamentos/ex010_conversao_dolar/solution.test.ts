import { describe, it, expect } from "vitest";
import { converterDolar } from "./solution";


describe('converterDolar', () => {
  it.each([
    [[327, 3.27], 100],
    [[100, 5], 20],
    [[0, 3.27], 0],
    [[3.27, 3.27], 1],
    [[3.27], 1],
    [[50, 5], 10],
    [[200, 4], 50],
    [[1, 2], 0.5],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = converterDolar(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
