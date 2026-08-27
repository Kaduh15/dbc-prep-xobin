import { describe, it, expect } from 'vitest';
import { dezTermosPa } from './solution';

describe('dezTermosPa', () => {
  it('caso 1', () => {
    expect(dezTermosPa(2, 3)).toEqual([2, 5, 8, 11, 14, 17, 20, 23, 26, 29]);
  });
  it('caso 2', () => {
    expect(dezTermosPa(1, 1)).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
  });
  it('caso 3', () => {
    expect(dezTermosPa(10, -2)).toEqual([10, 8, 6, 4, 2, 0, -2, -4, -6, -8]);
  });
});
