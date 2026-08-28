import { describe, it, expect } from "vitest";
import { temSilva } from "./solution";

describe("temSilva", () => {
  it.each([
    [["Jo\u00e3o Silva Pereira"], true],
    [["MARIA DA SILVA"], true],
    [["Ana Souza"], false],
    [["Silvania"], true],
    [[""], false],
    [["sILvA"], true],
    [["Jo\u00e3o sILVANIA"], true],
    [["Santo"], false],
    [["Silva Santos"], true],
    [["   da silva   "], true],
    [["Jos\u00e9"], false],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = temSilva(...(args as Parameters<typeof temSilva>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
