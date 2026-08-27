import { describe, it, expect } from "vitest";
import { novoSalario } from "./solution";

describe("novoSalario", () => {
  it("quinze", () => { expect(novoSalario(1000)).toBe(1150); });
  it("limiteQuinze", () => { expect(novoSalario(1250)).toBe(1437.5); });
  it("acimaLimite", () => { expect(novoSalario(1250.01)).toBe(1375.01); });
  it("dez", () => { expect(novoSalario(1500)).toBe(1650); });
  it("baixo", () => { expect(novoSalario(800)).toBe(920); });
});