import { describe, it, expect } from "vitest";
import { somaMultiplosDe3 } from "./solution";

describe("somaMultiplosDe3", () => {
  it.each([
    [[], 41583],
    [[1, 10], 18],
    [[5, 12], 27],
    [[1, 6], 9],
    [[3, 3], 3],
    [[0, 10], 18],
    [[10, 15], 27],
    [[1, 3], 3],
    [[100, 100], 0],
  ] as [number[], number][])("caso %#", (args, esperado) => {
    if (args.length === 0) expect(somaMultiplosDe3()).toEqual(esperado);
    else expect(somaMultiplosDe3(args[0], args[1])).toEqual(esperado);
  });
});
