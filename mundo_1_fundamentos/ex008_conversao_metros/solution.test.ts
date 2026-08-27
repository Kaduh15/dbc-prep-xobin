import { describe, it, expect } from 'vitest';
import { converterMetros } from './solution';

describe('converterMetros', () => {
  it('converte 1 metro', () => {
    expect(converterMetros(1)).toEqual([100, 1000]);
  });

  it('converte metros decimais', () => {
    expect(converterMetros(2.5)).toEqual([250, 2500]);
  });

  it('valor zero', () => {
    expect(converterMetros(0)).toEqual([0, 0]);
  });

  it('meio metro', () => {
    expect(converterMetros(0.5)).toEqual([50, 500]);
  });
});