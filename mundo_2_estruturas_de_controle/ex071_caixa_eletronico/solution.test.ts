import { describe, it, expect } from 'vitest';
import { caixaEletronico } from './solution';

describe('caixaEletronico', () => {
  it('caso 1', () => {
    expect(caixaEletronico(188)).toEqual({100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1});
  });
  it('caso 2', () => {
    expect(caixaEletronico(650)).toEqual({100: 6, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0});
  });
  it('caso 3', () => {
    expect(caixaEletronico(30)).toEqual({100: 0, 50: 0, 20: 1, 10: 1, 5: 0, 2: 0, 1: 0});
  });
  it('caso 4', () => {
    expect(caixaEletronico(0)).toEqual({100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0});
  });
});
