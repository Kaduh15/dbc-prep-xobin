import { describe, it, expect } from "vitest";
import { contarCaracteres } from "./solution";

describe("contarCaracteres", () => {
  it.each([
    [["banana"], {"b": 1, "a": 3, "n": 2}],
    [[""], {}],
    [["aA"], {"a": 1, "A": 1}],
    [["aba"], {"a": 2, "b": 1}]
])("caso", (args: any[], esperado: any) => {
    const resultado = contarCaracteres(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
