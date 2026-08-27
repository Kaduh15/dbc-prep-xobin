import { describe, it, expect } from 'vitest';
import { paContinua } from './solution';

describe('paContinua', () => {
  it('caso 1', () => {
    expect(paContinua(2, 3, [5])).toEqual([2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]);
  });
  it('caso 2', () => {
    expect(paContinua(2, 3, [])).toEqual([2, 5, 8, 11, 14, 17, 20, 23, 26, 29]);
  });
  it('caso 3', () => {
    expect(paContinua(2, 3, [3, 0])).toEqual([2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]);
  });
  it('caso 4', () => {
    expect(paContinua(2, 3, [0, 5])).toEqual([2, 5, 8, 11, 14, 17, 20, 23, 26, 29]);
  });
  it('caso 5', () => {
    expect(paContinua(1, 5, [2])).toEqual([1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56]);
  });
});
