import { describe, expect, it } from "vitest";
import { comecaComSanto } from "./solution";

describe("comecaComSanto", () => {
  it.each([["Santo Amaro", true],
    ["santos", true],
    ["SANTO ANDR\u00c9", true],
    ["  Santo Antonio  ", true],
    ["Porto Alegre", false],
    ["Rio de Janeiro", false],
    ["Santo", true],
    ["SANTOS", true],
    ["santorini", true],
    ["", false],
    ["Asantos", false]])
    ("comecaComSanto(%s) retorna %s", (cidade, esperado) => {
    expect(comecaComSanto(cidade)).toBe(esperado);
  });
});
