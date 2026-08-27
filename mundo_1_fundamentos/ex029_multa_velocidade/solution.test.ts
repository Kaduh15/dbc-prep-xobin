import { describe, it, expect } from "vitest";
import { multaVelocidade } from "./solution";

describe("multaVelocidade", () => {
  it("limite", () => { expect(multaVelocidade(80)).toBe(0.0); });
  it("umAcima", () => { expect(multaVelocidade(81)).toBe(7.0); });
  it("noventa", () => { expect(multaVelocidade(90)).toBe(70.0); });
  it("duzentos", () => { expect(multaVelocidade(200)).toBe(840.0); });
  it("abaixo", () => { expect(multaVelocidade(79.9)).toBe(0.0); });
  it("negativo", () => { expect(multaVelocidade(-5)).toBe(0.0); });
});
