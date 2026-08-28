import { describe, it, expect } from "vitest";
import { venceuAdivinhacao } from "./solution";

describe("venceuAdivinhacao", () => {
  it.each([
    [[3, 3], true],
    [[3, 5], false],
    [[0, 0], true],
    [[5, 0], false],
    [[5, 5], true],
    [[2, 3], false],
    [[0, 5], false],
    [[4, 4], true],
    [[1, 0], false],
    [[-1, -1], true],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = venceuAdivinhacao(...(args as Parameters<typeof venceuAdivinhacao>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
