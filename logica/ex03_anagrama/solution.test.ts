import { describe, it, expect } from "vitest";
import { anagrama } from "./solution";

describe("anagrama", () => {
  it.each([
    [["listen", "silent"], true],
    [["triangle", "integral"], true],
    [["cat", "dog"], false],
    [["hello", "hello"], true],
    [["", ""], true],
    [["a", "b"], false],
    [["anagram", "nag a ram"], true],
    [["python", "java"], false],
])("caso", (args: any[], esperado: any) => {
    const resultado = anagrama(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
