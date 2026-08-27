import { describe, it, expect } from "vitest";
import { palindromo } from "./solution";

describe("palindromo", () => {
  it.each([
    [["ana"], true],
    [["hello"], false],
    [["A man a plan a canal Panama"], true],
    [[""], true],
    [["anA"], true],
    [["never odd or even"], true],
    [["java"], false]
])("caso", (args: any[], esperado: any) => {
    const resultado = palindromo(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
