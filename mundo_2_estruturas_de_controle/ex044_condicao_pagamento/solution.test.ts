import { describe, it, expect } from "vitest";
import { valorFinal } from "./solution";

describe("valorFinal", () => {
  it.each([
    [[100, "dinheiro"], 90],
    [[100, "cartao_avista"], 95],
    [[100, "2x"], 100],
    [[100, "3x_mais"], 120],
    [[80, "dinheiro"], 72],
    [[0, "dinheiro"], 0],
    [[80, "cartao_avista"], 76],
    [[200, "2x"], 200],
    [[200, "3x_mais"], 240],
    [[50, "dinheiro"], 45],
    [[10, "cartao_avista"], 9.5],
  ] as [unknown[], number][])("caso %#", (args, esperado) => {
    expect(valorFinal(args[0] as number, args[1] as string)).toBe(esperado);
  });

  it("condicao invalida lanca", () => {
    expect(() => valorFinal(100, "parcelado")).toThrow();
    expect(() => valorFinal(100, "")).toThrow();
  });
});
