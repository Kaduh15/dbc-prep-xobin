import { describe, it, expect } from "vitest";
import { palindromo } from "./solution";

describe("palindromo", () => {
  it.each([
    [["arara"], true],
    [["A man a plan a canal Panama"], true],
    [["hello"], false],
    [[""], true],
    [["Ana"], true],
    [["12321"], true],
    [["a"], true],
    [["ab"], false],
])("caso", (args: any[], esperado: any) => {
    const resultado = palindromo(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
