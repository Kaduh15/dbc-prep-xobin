import { describe, it, expect } from 'vitest';
import { somaIgnorandoFlag } from './solution';

describe('somaIgnorandoFlag', () => {
  it('caso 1', () => {
    expect(somaIgnorandoFlag([2, 5, 999])).toEqual([2, 7]);
  });
  it('caso 2', () => {
    expect(somaIgnorandoFlag([1, 2, 3, 999])).toEqual([3, 6]);
  });
  it('caso 3', () => {
    expect(somaIgnorandoFlag([999])).toEqual([0, 0]);
  });
  it('caso 4', () => {
    expect(somaIgnorandoFlag([])).toEqual([0, 0]);
  });
});
