import { describe, it, expect } from "vitest";
import { analisePessoas } from "./solution";

describe("analisePessoas", () => {
  it.each([
    [[[[22, 'M'], [15, 'F'], [30, 'M'], [19, 'F']]], [3, 2, 2]],
    [[[[18, 'M'], [20, 'F']]], [1, 1, 0]],
    [[[[12, 'F']]], [0, 0, 1]],
    [[[]], [0, 0, 0]],
    [[[[25, 'f']]], [1, 0, 0]],
    [[[[17, 'f']]], [0, 0, 1]],
    [[[[18, 'F']]], [0, 0, 1]],
    [[[[20, 'F']]], [1, 0, 0]],
    [[[[30, 'X']]], [1, 0, 0]],
    [[[[19, 'M'], [21, 'F']]], [2, 1, 0]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = analisePessoas(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
