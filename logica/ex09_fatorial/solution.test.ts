import { describe, it, expect } from "vitest";
import { fatorial } from "./solution";

describe("fatorial", () => {
  it.each([
    [[0], 1],
    [[1], 1],
    [[5], 120],
    [[6], 720],
    [[10], 3628800]
])("caso", (args: any[], esperado: any) => {
    const resultado = fatorial(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
