import { describe, it, expect } from "vitest";
import { validarSexo } from "./solution";

describe("validarSexo", () => {
  it.each([
    ["M", true],
    ["F", true],
    ["m", false],
    ["f", false],
    ["X", false],
    ["", false],
    ["MF", false],
  ])("f(%j) -> %o", (sexo, esperado) => {
    expect(validarSexo(sexo)).toBe(esperado);
  });
});
