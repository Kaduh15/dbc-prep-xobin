import { describe, it, expect } from "vitest";
import { jokenpo } from "./solution";

describe("jokenpo", () => {
  it('jokenpo("pedra", "tesoura")', () => {
    expect(jokenpo("pedra", "tesoura")).toEqual('usuario');
  });
  it('jokenpo("tesoura", "papel")', () => {
    expect(jokenpo("tesoura", "papel")).toEqual('usuario');
  });
  it('jokenpo("papel", "pedra")', () => {
    expect(jokenpo("papel", "pedra")).toEqual('usuario');
  });
  it('jokenpo("tesoura", "pedra")', () => {
    expect(jokenpo("tesoura", "pedra")).toEqual('computador');
  });
  it('jokenpo("papel", "tesoura")', () => {
    expect(jokenpo("papel", "tesoura")).toEqual('computador');
  });
  it('jokenpo("pedra", "papel")', () => {
    expect(jokenpo("pedra", "papel")).toEqual('computador');
  });
  it('jokenpo("papel", "papel")', () => {
    expect(jokenpo("papel", "papel")).toEqual('empate');
  });
});
