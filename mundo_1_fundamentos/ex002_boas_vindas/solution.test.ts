import { describe, it, expect } from 'vitest';
import { boasVindas } from './solution';

describe('boasVindas', () => {
  it('saúda pelo nome', () => {
    expect(boasVindas('João')).toBe('Olá, João! Seja muito bem-vindo(a)!');
    expect(boasVindas('Maria')).toBe('Olá, Maria! Seja muito bem-vindo(a)!');
  });

  it('lida com nome vazio', () => {
    expect(boasVindas('')).toBe('Olá, ! Seja muito bem-vindo(a)!');
  });
});