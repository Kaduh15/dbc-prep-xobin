import { describe, it, expect } from "vitest";
import { analisarLetraA } from "./solution";

describe("analisarLetraA", () => {
  it.each([
    [["Arara Azul"], [4, 0, 6]],
    [["Mariana"], [3, 1, 6]],
    [["xyz"], [0, -1, -1]],
    [[""], [0, -1, -1]],
    [["AaA"], [3, 0, 2]],
    [["aaaa"], [4, 0, 3]],
    [["A"], [1, 0, 0]],
    [["a"], [1, 0, 0]],
    [["banana"], [3, 1, 5]],
    [["XYZYX"], [0, -1, -1]],
    [["casa amarela"], [5, 1, 11]],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = analisarLetraA(...(args as Parameters<typeof analisarLetraA>));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
