import { describe, it, expect } from "vitest";
import { ehPalindromo } from "./solution";

describe("ehPalindromo", () => {
  it.each([
    ["arara", true],
    ["Ana", true],
    ["a sacada da casa", true],
    ["socorram me subi no onibus em marrocos", true],
    ["Roma me tem amor", true],
    ["banana", false],
    ["palindromo", false],
    ["ovo", true],
    ["php", true],
    ["reviver", true],
    ["casa", false],
    ["", true],
  ])("f(...) -> %j",
    (frase, esperado) => {
      expect(ehPalindromo(frase)).toBe(esperado);
    });
  });