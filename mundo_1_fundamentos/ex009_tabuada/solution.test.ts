import { describe, it, expect } from 'vitest';
import { tabuada } from './solution';

describe('tabuada', () => {
  it('tabuada de 7', () => {
    expect(tabuada(7)).toEqual([7, 14, 21, 28, 35, 42, 49, 56, 63, 70]);
  });

  it('tabuada de 2', () => {
    expect(tabuada(2)).toEqual([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]);
  });

  it('tabuada de zero tem 10 elementos', () => {
    expect(tabuada(0)).toEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
  });

  it('tabuada negativa', () => {
    expect(tabuada(-3)).toEqual([-3, -6, -9, -12, -15, -18, -21, -24, -27, -30]);
  });
});