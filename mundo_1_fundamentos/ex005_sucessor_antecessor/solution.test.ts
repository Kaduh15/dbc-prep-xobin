import { describe, it, expect } from 'vitest';
import { sucessorAntecessor } from './solution';

describe('sucessorAntecessor', () => {
  it('retorna antecessor e sucessor para positivo', () => {
    expect(sucessorAntecessor(10)).toEqual([9, 11]);
  });

  it('lida com o zero', () => {
    expect(sucessorAntecessor(0)).toEqual([-1, 1]);
  });

  it('lida com negativo', () => {
    expect(sucessorAntecessor(-5)).toEqual([-6, -4]);
  });
});