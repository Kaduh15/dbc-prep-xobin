import { describe, it, expect } from "vitest";
import { mediaAproveitamento } from "./solution";

describe("mediaAproveitamento", () => {
  it('mediaAproveitamento(4, 4)', () => {
    expect(mediaAproveitamento(4, 4)).toEqual('Reprovado');
  });
  it('mediaAproveitamento(4, 6)', () => {
    expect(mediaAproveitamento(4, 6)).toEqual('Recuperacao');
  });
  it('mediaAproveitamento(5, 8)', () => {
    expect(mediaAproveitamento(5, 8)).toEqual('Recuperacao');
  });
  it('mediaAproveitamento(7, 7)', () => {
    expect(mediaAproveitamento(7, 7)).toEqual('Aprovado');
  });
  it('mediaAproveitamento(8, 10)', () => {
    expect(mediaAproveitamento(8, 10)).toEqual('Aprovado');
  });
});
