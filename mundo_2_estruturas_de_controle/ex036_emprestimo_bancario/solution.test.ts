import { describe, it, expect } from "vitest";
import { prestacaoMensal, aprovaEmprestimo } from "./solution";

describe("prestacaoMensal", () => {
  it("basica", () => { expect(prestacaoMensal(100000, 20)).toBe(416.6666666666667); });
  it("dozeMeses", () => { expect(prestacaoMensal(30000, 1)).toBe(2500); });
});

describe("aprovaEmprestimo", () => {
  it("aprovado", () => { expect(aprovaEmprestimo(100000, 2000, 20)).toBe(true); });
  it("negado", () => { expect(aprovaEmprestimo(200000, 2000, 20)).toBe(false); });
  it("salarioAlto", () => { expect(aprovaEmprestimo(120000, 5000, 10)).toBe(true); });
  it("prazoCurto", () => { expect(aprovaEmprestimo(80000, 1500, 10)).toBe(false); });
  it("limiteExato", () => { expect(aprovaEmprestimo(72000, 2000, 10)).toBe(true); });
});