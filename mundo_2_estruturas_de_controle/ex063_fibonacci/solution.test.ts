import { describe, it, expect } from 'vitest';
import { fibonacci } from './solution';

describe('fibonacci', () => {
  it('caso 1', () => {
    expect(fibonacci(0)).toEqual([]);
  });
  it('caso 2', () => {
    expect(fibonacci(1)).toEqual([0]);
  });
  it('caso 3', () => {
    expect(fibonacci(2)).toEqual([0, 1]);
  });
  it('caso 4', () => {
    expect(fibonacci(5)).toEqual([0, 1, 1, 2, 3]);
  });
  it('caso 5', () => {
    expect(fibonacci(10)).toEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]);
  });
});
