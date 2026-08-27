import { describe, it, expect } from 'vitest';
import { numerosAte999 } from './solution';

describe('numerosAte999', () => {
  it('caso 1', () => {
    expect(numerosAte999([5, 999])).toEqual([1, 5]);
  });
  it('caso 2', () => {
    expect(numerosAte999([7, 8, 999, 10])).toEqual([2, 15]);
  });
  it('caso 3', () => {
    expect(numerosAte999([999])).toEqual([0, 0]);
  });
  it('caso 4', () => {
    expect(numerosAte999([])).toEqual([0, 0]);
  });
});
