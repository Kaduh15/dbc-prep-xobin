import { describe, it, expect } from 'vitest';
import { estatisticas } from './solution';

describe('estatisticas', () => {
  it('caso 1', () => {
    expect(estatisticas([7, 5, 8, 3])).toEqual([5.75, 8, 3]);
  });
  it('caso 2', () => {
    expect(estatisticas([10])).toEqual([10.0, 10, 10]);
  });
  it('caso 3', () => {
    expect(estatisticas([2, 9, 4])).toEqual([5.0, 9, 2]);
  });
  it('caso 4', () => {
    expect(estatisticas([5, 5, 5, 5])).toEqual([5.0, 5, 5]);
  });
});
