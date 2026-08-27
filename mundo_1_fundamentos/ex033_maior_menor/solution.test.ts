import { describe, it, expect } from "vitest";
import { maiorEMenor } from "./solution";

describe("maiorEMenor", () => {
  it("ordemMista", () => { expect(maiorEMenor(3, 7, 5)).toEqual([7, 3]); });
  it("crescente", () => { expect(maiorEMenor(1, 2, 3)).toEqual([3, 1]); });
  it("decrescente", () => { expect(maiorEMenor(9, 5, 1)).toEqual([9, 1]); });
  it("negativos", () => { expect(maiorEMenor(-1, -5, -2)).toEqual([-1, -5]); });
  it("iguais", () => { expect(maiorEMenor(9, 9, 9)).toEqual([9, 9]); });
});