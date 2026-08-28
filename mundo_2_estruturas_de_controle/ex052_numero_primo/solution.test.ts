import { describe, it, expect } from "vitest";
import { ehPrimo } from "./solution";

describe("ehPrimo", () => {
  it.each([
    [2, true],
    [3, true],
    [7, true],
    [97, true],
    [1, false],
    [4, false],
    [12, false],
    [100, false],
    [0, false],
    [-5, false],
    [9, false],
    [91, false],
    [101, true],
    [997, true],
  ])("f(...) -> %j",
    (n, esperado) => {
      expect(ehPrimo(n)).toBe(esperado);
    });
  });