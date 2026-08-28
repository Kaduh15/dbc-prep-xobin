import { describe, it, expect } from "vitest";
import { fibonacci } from "./solution";

describe("fibonacci", () => {
  it.each([
    [[0], 0],
    [[1], 1],
    [[2], 1],
    [[5], 5],
    [[10], 55],
    [[6], 8],
])("caso", (args: any[], esperado: any) => {
    const resultado = fibonacci(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
