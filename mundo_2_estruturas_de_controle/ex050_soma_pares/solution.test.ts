import { describe, it, expect } from "vitest";
import { somaPares } from "./solution";

describe("somaPares", () => {
  it.each([
    [[1, 2, 3, 4, 5, 6], 12],
    [[2, 4, 6], 12],
    [[1, 3, 5], 0],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30],
    [[], 0],
    [[-2, 3, 4, -6], -4],
  ])("f(%j) -> %i", (numeros, esperado) => {
    expect(somaPares(numeros)).toBe(esperado);
  });
});
