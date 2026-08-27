import { describe, it, expect } from "vitest";
import { precoPassagem } from "./solution";

describe("precoPassagem", () => {
  it("ate200", () => { expect(precoPassagem(50)).toBe(25.0); });
  it("limite200", () => { expect(precoPassagem(200)).toBe(100.0); });
  it("poucoAcima", () => { expect(precoPassagem(201)).toBe(90.45); });
  it("longa", () => { expect(precoPassagem(500)).toBe(225.0); });
  it("zero", () => { expect(precoPassagem(0)).toBe(0.0); });
});
