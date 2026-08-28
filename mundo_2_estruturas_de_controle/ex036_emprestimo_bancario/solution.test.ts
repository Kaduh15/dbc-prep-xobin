import { describe, it, expect } from "vitest";
import { prestacaoMensal, aprovaEmprestimo } from "./solution";

describe("prestacaoMensal", () => {
  it.each([
    [[100000, 20], 416.6666666666667],
    [[30000, 1], 2500],
    [[240000, 20], 1000],
    [[12000, 1], 1000],
    [[100, 1], 8.333333333333334],
    [[0, 5], 0],
    [[600000, 50], 1000],
  ] as [number[], number][])("caso %#", (args, esperado) => {
    expect(prestacaoMensal(args[0], args[1])).toBe(esperado);
  });
});

describe("aprovaEmprestimo", () => {
  it.each([
    [[100000, 2000, 20], true],
    [[200000, 2000, 20], false],
    [[120000, 5000, 10], true],
    [[80000, 1500, 10], false],
    [[72000, 2000, 10], true],
    [[30000, 2000, 5], true],
    [[60000, 2000, 5], false],
    [[72001, 2000, 10], false],
    [[1000, 0, 10], false],
  ] as [number[], boolean][])("caso %#", (args, esperado) => {
    expect(aprovaEmprestimo(args[0], args[1], args[2])).toBe(esperado);
  });
});
