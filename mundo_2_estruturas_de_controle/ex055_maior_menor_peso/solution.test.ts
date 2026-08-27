import { describe, it, expect } from "vitest";
import { maiorMenorPeso } from "./solution";

describe("maiorMenorPeso", () => {
  it.each([
    [[70.5, 80.0, 55.3, 90.2, 62.1], [90.2, 55.3]],
    [[50.0, 50.0], [50.0, 50.0]],
    [[100.0, 20.0, 40.0], [100.0, 20.0]],
    [[65.0, 65.0, 65.0], [65.0, 65.0]],
  ])("f(%j) -> %j", (pesos, esperado) => {
    expect(maiorMenorPeso(pesos)).toEqual(esperado);
  });
});
