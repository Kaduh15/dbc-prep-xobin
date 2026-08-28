import { describe, it, expect } from "vitest";
import { novoSalario } from "./solution";

describe("novoSalario", () => {
  it.each([
    [[1000], 1150.0],
    [[1250], 1437.5],
    [[1250.01], 1375.01],
    [[1500], 1650.0],
    [[800], 920.0],
    [[0], 0.0],
    [[2000], 2200.0],
    [[10000], 11000.0],
    [[10], 11.5],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = novoSalario(...(args as Parameters<typeof novoSalario>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
