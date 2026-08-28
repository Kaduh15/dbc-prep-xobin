import { describe, it, expect } from "vitest";
import { jokenpo } from "./solution";

describe("jokenpo", () => {
  it.each([
    [["pedra", "tesoura"], "usuario"],
    [["tesoura", "papel"], "usuario"],
    [["papel", "pedra"], "usuario"],
    [["tesoura", "pedra"], "computador"],
    [["papel", "tesoura"], "computador"],
    [["pedra", "papel"], "computador"],
    [["papel", "papel"], "empate"],
    [["pedra", "pedra"], "empate"],
    [["tesoura", "tesoura"], "empate"],
  ] as [string[], string][])("caso %#", (args, esperado) => {
    expect(jokenpo(args[0], args[1])).toEqual(esperado);
  });

  it("jogada invalida lanca", () => {
    expect(() => jokenpo("lagarto", "papel")).toThrow();
    expect(() => jokenpo("pedra", "lagarto")).toThrow();
  });
});
