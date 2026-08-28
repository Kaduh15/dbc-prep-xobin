import { describe, expect, it } from "vitest";
import { hipotenusa } from "./solution";

describe("hipotenusa", () => {
  it.each([[3, 4, 5.0],
    [6, 8, 10.0],
    [5, 12, 13.0],
    [1, 1, 1.4142135623730951],
    [0, 6, 6.0],
    [0, 0, 0.0],
    [7, 24, 25.0],
    [20, 21, 29.0]])
    ("hipotenusa(%d, %d) retorna %d", (catO, catAd, esperado) => {
    expect(hipotenusa(catO, catAd)).toBeCloseTo(esperado, 10);
  });
});
