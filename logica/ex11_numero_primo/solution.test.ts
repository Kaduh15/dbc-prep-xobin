import { describe, it, expect } from "vitest";
import { numeroPrimo } from "./solution";

describe("numeroPrimo", () => {
  it.each([
    [[0], false],
    [[1], false],
    [[2], true],
    [[3], true],
    [[4], false],
    [[9], false],
    [[97], true],
    [[25], false],
])("caso", (args: any[], esperado: any) => {
    const resultado = numeroPrimo(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
