import { describe, it, expect } from "vitest";
import { precoPassagem } from "./solution";

describe("precoPassagem", () => {
  it.each([
    [[50], 25.0],
    [[200], 100.0],
    [[201], 90.45],
    [[500], 225.0],
    [[0], 0.0],
    [[199.9], 99.95],
    [[1000], 450.0],
    [[199], 99.5],
    [[1], 0.5],
    [[250], 112.5],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = precoPassagem(...(args as Parameters<typeof precoPassagem>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
