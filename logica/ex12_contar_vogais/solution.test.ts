import { describe, it, expect } from "vitest";
import { contarVogais } from "./solution";

describe("contarVogais", () => {
  it.each([
    [["hello"], 2],
    [["Banana"], 3],
    [["xyz"], 0],
    [["AEIOU"], 5],
    [[""], 0],
    [["ritmo"], 2]
])("caso", (args: any[], esperado: any) => {
    const resultado = contarVogais(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
