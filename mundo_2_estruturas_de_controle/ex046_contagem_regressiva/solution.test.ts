import { describe, it, expect } from "vitest";
import { contagemRegressiva } from "./solution";

describe("contagemRegressiva", () => {
  it.each([
    [[], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],
    [[3], [3, 2, 1, 0]],
    [[0], [0]],
    [[1], [1, 0]],
    [[5], [5, 4, 3, 2, 1, 0]],
    [[2], [2, 1, 0]],
  ] as [number[], number[]][])("caso %#", (args, esperado) => {
    if (args.length === 0) expect(contagemRegressiva()).toEqual(esperado);
    else expect(contagemRegressiva(args[0])).toEqual(esperado);
  });
});
