import { describe, it, expect } from "vitest";
import { inverterString } from "./solution";

describe("inverterString", () => {
  it.each([
    [["hello"], "olleh"],
    [[""], ""],
    [["abc"], "cba"],
    [["a"], "a"],
    [["a man"], "nam a"],
    [["ol\u00e1 mundo"], "odnum \u00e1lo"],
])("caso", (args: any[], esperado: any) => {
    const resultado = inverterString(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
