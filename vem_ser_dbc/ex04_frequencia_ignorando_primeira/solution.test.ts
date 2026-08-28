import { describe, it, expect } from "vitest";
import { frequenciaIgnorandoPrimeira } from "./solution";

describe("frequenciaIgnorandoPrimeira", () => {
  it.each([
    [[""], {}],
    [["abc"], {}],
    [["aab"], {"a": 1}],
    [["aaaa"], {"a": 3}],
    [["banana"], {"a": 2, "n": 1}],
    [["aa bb"], {"a": 1, "b": 1}],
])("caso", (args: any, esperado: any) => {
    const resultado = frequenciaIgnorandoPrimeira(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
