import { describe, it, expect } from 'vitest';
import { somar } from './solution';

describe('somar', () => {
  it('soma números positivos', () => {
    expect(somar(2, 5)).toBe(7);
  });

  it('soma números negativos', () => {
    expect(somar(-3, 8)).toBe(5);
  });

  it('soma decimais', () => {
    expect(somar(1.5, 2.5)).toBeCloseTo(4.0);
  });

  it('soma zeros', () => {
    expect(somar(0, 0)).toBe(0);
  });
});