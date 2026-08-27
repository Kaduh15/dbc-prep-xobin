import { describe, it, expect } from 'vitest';
import { parOuImpar } from './solution';

describe('parOuImpar', () => {
  it('caso 1', () => {
    expect(parOuImpar(4, 2, "par")).toEqual(true);
  });
  it('caso 2', () => {
    expect(parOuImpar(5, 4, "impar")).toEqual(true);
  });
  it('caso 3', () => {
    expect(parOuImpar(4, 2, "impar")).toEqual(false);
  });
  it('caso 4', () => {
    expect(parOuImpar(3, 4, "par")).toEqual(false);
  });
  it('caso 5', () => {
    expect(parOuImpar(7, 3, "par")).toEqual(true);
  });
});
