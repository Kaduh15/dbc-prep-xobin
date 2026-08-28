import { describe, it, expect } from "vitest";
import { contarVogais } from "./solution";

describe("contarVogais", () => {
  it.each([
    [["hello"], 2],
    [[""], 0],
    [["AEIOU"], 5],
    [["try"], 0],
    [["banana"], 3],
    [["Ol\u00e1"], 1],
])("caso", (args: any[], esperado: any) => {
    const resultado = contarVogais(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
