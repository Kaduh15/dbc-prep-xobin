import { describe, it, expect } from "vitest";
import { fibonacci } from "./solution";

describe("fibonacci", () => {
  it.each([
    [[0], 0],
    [[1], 1],
    [[2], 1],
    [[10], 55],
    [[15], 610]
])("caso", (args: any[], esperado: any) => {
    const resultado = fibonacci(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
