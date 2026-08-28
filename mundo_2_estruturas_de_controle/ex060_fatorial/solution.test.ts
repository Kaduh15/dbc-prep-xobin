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
    [2, 2],
    [4, 24],
    [7, 5040],
    [12, 479001600],
  ])("f(...) -> %j",
    (n, esperado) => {
      expect(fatorial(n)).toBe(esperado);
    });
  });