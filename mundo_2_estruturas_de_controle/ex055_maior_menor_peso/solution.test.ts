import { describe, it, expect } from "vitest";
import { maiorMenorPeso } from "./solution";

describe("maiorMenorPeso", () => {
  it.each([
    [[70.5, 80, 55.3, 90.2, 62.1], [90.2, 55.3]],
    [[50, 50], [50, 50]],
    [[100, 20, 40], [100, 20]],
    [[65, 65, 65], [65, 65]],
    [[42], [42, 42]],
    [[20, 100, 40], [100, 20]],
    [[0.5, 0.1, 0.9], [0.9, 0.1]],
  ])("f(...) -> %j",
    (pesos, esperado) => {
      expect(maiorMenorPeso(pesos)).toEqual(esperado);
    });
  });