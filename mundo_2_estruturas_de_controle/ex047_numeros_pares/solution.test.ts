import { describe, it, expect } from "vitest";
import { numerosPares } from "./solution";

describe("numerosPares", () => {
  it('numerosPares()', () => {
    expect(numerosPares()).toEqual([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]);
  });
  it('numerosPares(1, 10)', () => {
    expect(numerosPares(1, 10)).toEqual([2, 4, 6, 8, 10]);
  });
  it('numerosPares(15, 25)', () => {
    expect(numerosPares(15, 25)).toEqual([16, 18, 20, 22, 24]);
  });
  it('numerosPares(3, 3)', () => {
    expect(numerosPares(3, 3)).toEqual([]);
  });
  it('numerosPares(2, 8)', () => {
    expect(numerosPares(2, 8)).toEqual([2, 4, 6, 8]);
  });
});
