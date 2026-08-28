import { describe, it, expect } from "vitest";
import { numerosPares } from "./solution";

describe("numerosPares", () => {
  it.each([
    [[], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]],
    [[1, 10], [2, 4, 6, 8, 10]],
    [[15, 25], [16, 18, 20, 22, 24]],
    [[3, 3], []],
    [[2, 8], [2, 4, 6, 8]],
    [[0, 6], [0, 2, 4, 6]],
    [[1, 1], []],
    [[7, 7], []],
    [[20, 30], [20, 22, 24, 26, 28, 30]],
  ] as [number[], number[]][])("caso %#", (args, esperado) => {
    if (args.length === 0) expect(numerosPares()).toEqual(esperado);
    else expect(numerosPares(args[0], args[1])).toEqual(esperado);
  });
});
