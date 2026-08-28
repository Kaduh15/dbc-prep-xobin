import { describe, it, expect } from "vitest";
import { olaMundo } from "./solution";


describe('olaMundo', () => {
  it.each([
    [[], "Olá, mundo!"],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = olaMundo(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
  it("é determinística", () => {
    const a = olaMundo();
    const b = olaMundo();
    expect(typeof a).toBe("string");
    expect(a).toBe(b);
  });
});
