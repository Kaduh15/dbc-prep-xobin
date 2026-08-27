import { describe, it, expect } from 'vitest';
import { dobroTriploRaiz } from './solution';

describe('dobroTriploRaiz', () => {
  it('calcula dobro, triplo e raiz', () => {
    expect(dobroTriploRaiz(9)).toEqual([18, 27, 3]);
  });

  it('calcula para quadrado perfeito', () => {
    expect(dobroTriploRaiz(4)).toEqual([8, 12, 2]);
  });

  it('lida com zero', () => {
    expect(dobroTriploRaiz(0)).toEqual([0, 0, 0]);
  });

  it('raiz não inteira com aproximação', () => {
    const [d, t, r] = dobroTriploRaiz(2);
    expect(d).toBe(4);
    expect(t).toBe(6);
    expect(r).toBeCloseTo(1.4142135623730951, 10);
  });
});