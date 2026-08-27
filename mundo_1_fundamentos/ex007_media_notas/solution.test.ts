import { describe, it, expect } from 'vitest';
import { mediaNotas } from './solution';

describe('mediaNotas', () => {
  it('notas iguais', () => {
    expect(mediaNotas(7, 7)).toBe(7);
  });

  it('notas decimais', () => {
    expect(mediaNotas(5.5, 8.5)).toBeCloseTo(7.0);
  });

  it('média com valores variados', () => {
    expect(mediaNotas(10, 2)).toBe(6);
  });

  it('zeros', () => {
    expect(mediaNotas(0, 0)).toBe(0);
  });
});