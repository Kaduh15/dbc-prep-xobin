import { describe, it, expect } from "vitest";
import { mediaAproveitamento } from "./solution";

describe("mediaAproveitamento", () => {
  it.each([
    [[4, 4], "Reprovado"],
    [[4, 6], "Recuperacao"],
    [[5, 8], "Recuperacao"],
    [[7, 7], "Aprovado"],
    [[8, 10], "Aprovado"],
    [[5, 5], "Recuperacao"],
    [[6, 7], "Recuperacao"],
    [[8, 6], "Aprovado"],
    [[0, 0], "Reprovado"],
    [[10, 10], "Aprovado"],
    [[3, 6], "Reprovado"],
  ] as [number[], string][])("caso %#", (args, esperado) => {
    expect(mediaAproveitamento(args[0], args[1])).toEqual(esperado);
  });
});
