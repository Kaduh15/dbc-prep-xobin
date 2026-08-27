import { describe, it, expect } from 'vitest';
import { converterDolar } from './solution';

describe('converterDolar', () => {
  it('converte com cotação explícita', () => {
    expect(converterDolar(327, 3.27)).toBeCloseTo(100.0, 6);
  });

  it('converte 100 reais a 5.0', () => {
    expect(converterDolar(100, 5.0)).toBeCloseTo(20.0, 6);
  });

  it('zero reais', () => {
    expect(converterDolar(0, 3.27)).toBeCloseTo(0.0, 6);
  });

  it('usa cotação padrão 3.27', () => {
    expect(converterDolar(3.27)).toBeCloseTo(1.0, 6);
  });
});