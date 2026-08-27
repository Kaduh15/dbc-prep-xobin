import { describe, it, expect } from "vitest";
import { primeiroUltimoNome } from "./solution";

describe("primeiroUltimoNome", () => {
  it("doisNomes", () => { expect(primeiroUltimoNome("João Silva")).toEqual(["João", "Silva"]); });
  it("tresNomes", () => { expect(primeiroUltimoNome("Maria Clara Souza")).toEqual(["Maria", "Souza"]); });
  it("nomeUnico", () => { expect(primeiroUltimoNome("Ana")).toEqual(["Ana", "Ana"]); });
  it("espacosExtra", () => { expect(primeiroUltimoNome("  Pedro  Henrique  ")).toEqual(["Pedro", "Henrique"]); });
});