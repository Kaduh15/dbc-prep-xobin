import { describe, it, expect } from "vitest";
import { contagemRegressiva } from "./solution";

describe("contagemRegressiva", () => {
  it('contagemRegressiva()', () => {
    expect(contagemRegressiva()).toEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]);
  });
  it('contagemRegressiva(3)', () => {
    expect(contagemRegressiva(3)).toEqual([3, 2, 1, 0]);
  });
  it('contagemRegressiva(0)', () => {
    expect(contagemRegressiva(0)).toEqual([0]);
  });
});
