import { describe, it, expect } from "vitest";
import { situacaoAlistamento } from "./solution";

describe("situacaoAlistamento", () => {
  it('situacaoAlistamento(16)', () => {
    expect(situacaoAlistamento(16)).toEqual('faltam 2 anos');
  });
  it('situacaoAlistamento(17)', () => {
    expect(situacaoAlistamento(17)).toEqual('faltam 1 ano');
  });
  it('situacaoAlistamento(18)', () => {
    expect(situacaoAlistamento(18)).toEqual('hora de se alistar');
  });
  it('situacaoAlistamento(21)', () => {
    expect(situacaoAlistamento(21)).toEqual('ja passou 3 anos');
  });
  it('situacaoAlistamento(30)', () => {
    expect(situacaoAlistamento(30)).toEqual('ja passou 12 anos');
  });
});
