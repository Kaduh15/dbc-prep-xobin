import { describe, it, expect } from "vitest";
import { venceuAdivinhacao } from "./solution";

describe("venceuAdivinhacao", () => {
  it("acertou", () => { expect(venceuAdivinhacao(3, 3)).toBe(true); });
  it("errou", () => { expect(venceuAdivinhacao(3, 5)).toBe(false); });
  it("zero", () => { expect(venceuAdivinhacao(0, 0)).toBe(true); });
  it("diferenteLimite", () => { expect(venceuAdivinhacao(5, 0)).toBe(false); });
});
