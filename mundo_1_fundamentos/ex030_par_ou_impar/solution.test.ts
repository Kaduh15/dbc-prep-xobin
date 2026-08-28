import { describe, it, expect } from "vitest";
import { parOuImpar } from "./solution";

describe("parOuImpar", () => {
  it.each([
    [[2], "PAR"],
    [[3], "\u00cdMPAR"],
    [[0], "PAR"],
    [[-4], "PAR"],
    [[-7], "\u00cdMPAR"],
    [[1], "\u00cdMPAR"],
    [[-2], "PAR"],
    [[-1], "\u00cdMPAR"],
    [[4], "PAR"],
    [[100], "PAR"],
    [[101], "\u00cdMPAR"],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = parOuImpar(...(args as Parameters<typeof parOuImpar>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
