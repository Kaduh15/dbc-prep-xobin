import { describe, it, expect } from 'vitest';
import { olaMundo } from './solution';

describe('olaMundo', () => {
  it('retorna a mensagem clássica', () => {
    expect(olaMundo()).toBe('Olá, mundo!');
  });
});