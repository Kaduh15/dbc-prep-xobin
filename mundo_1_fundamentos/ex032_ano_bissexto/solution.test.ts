import { describe, it, expect } from "vitest";
import { ehBissexto } from "./solution";

describe("ehBissexto", () => {
  it("ano2024", () => { expect(ehBissexto(2024)).toBe(true); });
  it("ano2023", () => { expect(ehBissexto(2023)).toBe(false); });
  it("ano2000", () => { expect(ehBissexto(2000)).toBe(true); });
  it("ano1900", () => { expect(ehBissexto(1900)).toBe(false); });
  it("ano1600", () => { expect(ehBissexto(1600)).toBe(true); });
  it("quatro", () => { expect(ehBissexto(4)).toBe(true); });
});
