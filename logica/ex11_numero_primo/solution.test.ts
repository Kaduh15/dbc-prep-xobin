import { describe, it, expect } from "vitest";
import { numeroPrimo } from "./solution";

describe("numeroPrimo", () => {
  it.each([
    [[1], false],
    [[2], true],
    [[3], true],
    [[4], false],
    [[17], true],
    [[97], true],
    [[100], false]
])("caso", (args: any[], esperado: any) => {
    const resultado = numeroPrimo(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
