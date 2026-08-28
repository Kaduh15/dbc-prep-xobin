import { describe, it, expect } from "vitest";
import { analiseProdutos } from "./solution";

describe("analiseProdutos", () => {
  it.each([
    [[[['Borracha', 2], ['Caderno', 15], ['Mouse', 120]]], [137.0, 2, 'Borracha']],
    [[[['X', 100.0]]], [100.0, 0, 'X']],
    [[[['A', 5], ['B', 3]]], [8.0, 2, 'B']],
    [[[]], [0.0, 0, '']],
    [[[['A', 99.5], ['B', 100]]], [199.5, 1, 'A']],
    [[[['A', 5], ['B', 5]]], [10.0, 2, 'A']],
    [[[['Copo', 7.5], ['Lapis', 1.5]]], [9.0, 2, 'Lapis']],
    [[[['Z', 0]]], [0.0, 1, 'Z']],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = analiseProdutos(...args);
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
