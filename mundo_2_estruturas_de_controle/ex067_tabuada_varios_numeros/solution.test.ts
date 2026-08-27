import { describe, it, expect } from 'vitest';
import { tabuada } from './solution';

describe('tabuada', () => {
  it('caso 1', () => {
    expect(tabuada(7)).toEqual([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70]);
  });
  it('caso 2', () => {
    expect(tabuada(5)).toEqual([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]);
  });
  it('caso 3', () => {
    expect(tabuada(-3)).toEqual(null);
  });
  it('caso 4', () => {
    expect(tabuada(0)).toEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
  });
});
