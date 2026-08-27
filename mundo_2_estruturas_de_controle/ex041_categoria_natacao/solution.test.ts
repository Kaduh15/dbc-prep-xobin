import { describe, it, expect } from "vitest";
import { categoriaNatacao } from "./solution";

describe("categoriaNatacao", () => {
  it('categoriaNatacao(9)', () => {
    expect(categoriaNatacao(9)).toEqual('Mirim');
  });
  it('categoriaNatacao(14)', () => {
    expect(categoriaNatacao(14)).toEqual('Infantil');
  });
  it('categoriaNatacao(17)', () => {
    expect(categoriaNatacao(17)).toEqual('Junior');
  });
  it('categoriaNatacao(19)', () => {
    expect(categoriaNatacao(19)).toEqual('Junior');
  });
  it('categoriaNatacao(20)', () => {
    expect(categoriaNatacao(20)).toEqual('Senior');
  });
  it('categoriaNatacao(25)', () => {
    expect(categoriaNatacao(25)).toEqual('Master');
  });
});
