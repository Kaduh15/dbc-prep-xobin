import { describe, it, expect } from "vitest";
import { inverterString } from "./solution";

describe("inverterString", () => {
  it.each([
    [["abc"], "cba"],
    [["a"], "a"],
    [[""], ""],
    [["javascript"], "tpircsavaj"],
    [["Olá"], "álO"]
])("caso", (args: any[], esperado: any) => {
    const resultado = inverterString(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
