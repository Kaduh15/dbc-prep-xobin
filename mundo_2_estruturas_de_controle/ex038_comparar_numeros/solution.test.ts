import { describe, it, expect } from "vitest";
import { compararNumeros } from "./solution";

describe("compararNumeros", () => {
  it('compararNumeros(5, 2)', () => {
    expect(compararNumeros(5, 2)).toEqual('primeiro maior');
  });
  it('compararNumeros(2, 5)', () => {
    expect(compararNumeros(2, 5)).toEqual('segundo maior');
  });
  it('compararNumeros(3, 3)', () => {
    expect(compararNumeros(3, 3)).toEqual('iguais');
  });
  it('compararNumeros(-1, 4)', () => {
    expect(compararNumeros(-1, 4)).toEqual('segundo maior');
  });
  it('compararNumeros(-2, -2)', () => {
    expect(compararNumeros(-2, -2)).toEqual('iguais');
  });
});
