import { describe, it, expect } from "vitest";
import { fatorial } from "./solution";

describe("fatorial", () => {
  it.each([
    [5, 120],
    [0, 1],
    [1, 1],
    [3, 6],
    [10, 3628800],
    [6, 720],
  ])("f(%i) -> %i", (n, esperado) => {
    expect(fatorial(n)).toBe(esperado);
  });
});
