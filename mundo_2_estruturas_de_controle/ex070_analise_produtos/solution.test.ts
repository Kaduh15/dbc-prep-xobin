import { describe, it, expect } from 'vitest';
import { analiseProdutos } from './solution';

describe('analiseProdutos', () => {
  it('caso 1', () => {
    expect(analiseProdutos([("Borracha", 2), ("Caderno", 15), ("Mouse", 120)])).toEqual([137.0, 2, "Borracha"]);
  });
  it('caso 2', () => {
    expect(analiseProdutos([("X", 100.0)])).toEqual([100.0, 0, "X"]);
  });
  it('caso 3', () => {
    expect(analiseProdutos([("A", 5), ("B", 3)])).toEqual([8.0, 2, "B"]);
  });
  it('caso 4', () => {
    expect(analiseProdutos([])).toEqual([0.0, 0, ""]);
  });
});
