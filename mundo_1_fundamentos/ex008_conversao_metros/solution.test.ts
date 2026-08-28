import { describe, it, expect } from "vitest";
import { converterMetros } from "./solution";


describe('converterMetros', () => {
  it.each([
    [[1], [100, 1000]],
    [[2.5], [250, 2500]],
    [[0], [0, 0]],
    [[0.5], [50, 500]],
    [[0.25], [25, 250]],
    [[10], [1000, 10000]],
    [[1.5], [150, 1500]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = converterMetros(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
