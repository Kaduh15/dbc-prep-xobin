import { describe, it, expect } from "vitest";
import { anagrama } from "./solution";

describe("anagrama", () => {
  it.each([
    [["listen", "silent"], true],
    [["ana", "naa"], true],
    [["hello", "world"], false],
    [["", ""], true],
    [["aabb", "abab"], true],
    [["abc", "abcd"], false]
])("caso", (args: any[], esperado: any) => {
    const resultado = anagrama(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
