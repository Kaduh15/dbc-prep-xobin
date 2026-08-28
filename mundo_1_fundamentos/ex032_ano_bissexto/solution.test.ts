import { describe, it, expect } from "vitest";
import { ehBissexto } from "./solution";

describe("ehBissexto", () => {
  it.each([
    [[2024], true],
    [[2023], false],
    [[2000], true],
    [[1900], false],
    [[1600], true],
    [[4], true],
    [[1700], false],
    [[2100], false],
    [[0], true],
    [[400], true],
    [[1996], true],
    [[1], false],
    [[100], false],
    [[700], false],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = ehBissexto(...(args as Parameters<typeof ehBissexto>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
