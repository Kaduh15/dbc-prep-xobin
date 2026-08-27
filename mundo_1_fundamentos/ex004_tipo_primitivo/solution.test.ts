import { describe, it, expect } from 'vitest';
import { analisarValor } from './solution';

describe('analisarValor', () => {
  it('analisa uma palavra capitalizada', () => {
    expect(analisarValor('Python')).toEqual({
      tipo: 'str',
      so_espacos: false,
      e_numero: false,
      e_alfabetico: true,
      e_alfanumerico: true,
      em_maiusculas: false,
      em_minusculas: true,
      capitalizada: true,
    });
  });

  it('analisa uma string numérica', () => {
    expect(analisarValor('1234')).toEqual({
      tipo: 'str',
      so_espacos: false,
      e_numero: true,
      e_alfabetico: false,
      e_alfanumerico: true,
      em_maiusculas: false,
      em_minusculas: false,
      capitalizada: false,
    });
  });

  it('analisa string composta apenas por espaços', () => {
    expect(analisarValor('   ')).toEqual({
      tipo: 'str',
      so_espacos: true,
      e_numero: false,
      e_alfabetico: false,
      e_alfanumerico: false,
      em_maiusculas: false,
      em_minusculas: false,
      capitalizada: false,
    });
  });

  it('analisa string vazia', () => {
    expect(analisarValor('')).toEqual({
      tipo: 'str',
      so_espacos: false,
      e_numero: false,
      e_alfabetico: false,
      e_alfanumerico: false,
      em_maiusculas: false,
      em_minusculas: false,
      capitalizada: false,
    });
  });
});