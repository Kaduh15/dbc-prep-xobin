import { describe, it, expect } from "vitest";
import { temSilva } from "./solution";

describe("temSilva", () => {
  it("comSilva", () => { expect(temSilva("João Silva Pereira")).toBe(true); });
  it("maisMinusculas", () => { expect(temSilva("MARIA DA SILVA")).toBe(true); });
  it("semSilva", () => { expect(temSilva("Ana Souza")).toBe(false); });
  it("substring", () => { expect(temSilva("Silvania")).toBe(true); });
  it("vazio", () => { expect(temSilva("")).toBe(false); });
});
