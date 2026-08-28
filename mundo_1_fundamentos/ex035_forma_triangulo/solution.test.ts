import { describe, it, expect } from "vitest";
import { formaTriangulo } from "./solution";

describe("formaTriangulo", () => {
  it.each([
    [[3, 4, 5], true],
    [[1, 2, 3], false],
    [[10, 1, 1], false],
    [[5.5, 5.5, 5.5], true],
    [[7, 2, 4], false],
    [[2, 3, 4], true],
    [[1, 1, 1], true],
    [[2, 2, 4], false],
    [[3, 3, 6], false],
    [[5, 5, 10], false],
    [[1, 1, 2], false],
    [[1, 1, 1.999], true],
    [[0.1, 0.1, 0.1], true],
    [[3, 3, 5.999], true],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = formaTriangulo(...(args as Parameters<typeof formaTriangulo>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
