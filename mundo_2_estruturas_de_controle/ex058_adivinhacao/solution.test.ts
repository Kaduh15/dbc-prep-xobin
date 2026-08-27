import { describe, it, expect } from "vitest";
import { palpitesParaAcertar } from "./solution";

describe("palpitesParaAcertar", () => {
  it.each([
    [5, [8, 2, 5, 9], 3],
    [3, [1, 2, 3], 3],
    [7, [7], 1],
    [9, [1, 2, 3], 3],
    [4, [4, 4], 1],
  ])("f(%i, %j) -> %i", (numero, tentativas, esperado) => {
    expect(palpitesParaAcertar(numero, tentativas)).toBe(esperado);
  });
});
