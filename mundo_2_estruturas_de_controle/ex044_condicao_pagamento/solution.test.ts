import { describe, it, expect } from "vitest";
import { valorFinal } from "./solution";

describe("valorFinal", () => {
  it('valorFinal(100, "dinheiro")', () => {
    expect(valorFinal(100, "dinheiro")).toEqual(90.0);
  });
  it('valorFinal(100, "cartao_avista")', () => {
    expect(valorFinal(100, "cartao_avista")).toEqual(95.0);
  });
  it('valorFinal(100, "2x")', () => {
    expect(valorFinal(100, "2x")).toEqual(100.0);
  });
  it('valorFinal(100, "3x_mais")', () => {
    expect(valorFinal(100, "3x_mais")).toEqual(120.0);
  });
  it('valorFinal(80, "dinheiro")', () => {
    expect(valorFinal(80, "dinheiro")).toEqual(72.0);
  });
});
