import { describe, it, expect } from "vitest";
import { fibonacci } from "./solution";

describe("fibonacci", () => {
  it.each([
    [[0], []],
    [[1], [0]],
    [[2], [0, 1]],
    [[5], [0, 1, 1, 2, 3]],
    [[10], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]],
    [[6], [0, 1, 1, 2, 3, 5]],
    [[7], [0, 1, 1, 2, 3, 5, 8]],
    [[-3], []],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = fibonacci(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
