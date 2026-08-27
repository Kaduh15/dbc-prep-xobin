import { describe, it, expect } from 'vitest';
import { analisePessoas } from './solution';

describe('analisePessoas', () => {
  it('caso 1', () => {
    expect(analisePessoas([(22, "M"), (15, "F"), (30, "M"), (19, "F")])).toEqual([3, 2, 2]);
  });
  it('caso 2', () => {
    expect(analisePessoas([(18, "M"), (20, "F")])).toEqual([1, 1, 0]);
  });
  it('caso 3', () => {
    expect(analisePessoas([(12, "F")])).toEqual([0, 0, 1]);
  });
  it('caso 4', () => {
    expect(analisePessoas([])).toEqual([0, 0, 0]);
  });
});
