import { describe, it, expect } from 'vitest';
import { calcularTinta } from './solution';

describe('calcularTinta', () => {
  it('parede 2x2', () => {
    expect(calcularTinta(2, 2)).toEqual([4, 2]);
  });

  it('parede 7x4', () => {
    expect(calcularTinta(7, 4)).toEqual([28, 14]);
  });

  it('área zero', () => {
    expect(calcularTinta(0, 5)).toEqual([0, 0]);
  });

  it('dimensões decimais', () => {
    expect(calcularTinta(2.5, 4)).toEqual([10, 5]);
  });
});