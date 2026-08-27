import { describe, it, expect } from 'vitest';
import { precoComDesconto } from './solution';

describe('precoComDesconto', () => {
  it('desconto padrão de 5%', () => {
    expect(precoComDesconto(100)).toBeCloseTo(95.0, 6);
  });

  it('desconto padrão em outro valor', () => {
    expect(precoComDesconto(80)).toBeCloseTo(76.0, 6);
  });

  it('desconto explícito de 10%', () => {
    expect(precoComDesconto(100, 0.10)).toBeCloseTo(90.0, 6);
  });

  it('preço zero', () => {
    expect(precoComDesconto(0, 0.05)).toBe(0);
  });
});