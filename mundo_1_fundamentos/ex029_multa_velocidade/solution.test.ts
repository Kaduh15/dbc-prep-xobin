import { describe, it, expect } from "vitest";
import { multaVelocidade } from "./solution";

describe("multaVelocidade", () => {
  it.each([
    [[80], 0.0],
    [[81], 7.0],
    [[90], 70.0],
    [[200], 840.0],
    [[79.9], 0.0],
    [[-5], 0.0],
    [[0], 0.0],
    [[81.5], 10.5],
    [[80.5], 3.5],
    [[100], 140.0],
    [[79], 0.0],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = multaVelocidade(...(args as Parameters<typeof multaVelocidade>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
