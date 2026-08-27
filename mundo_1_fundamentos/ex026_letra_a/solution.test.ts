import { describe, it, expect } from "vitest";
import { analisarLetraA } from "./solution";

describe("analisarLetraA", () => {
  it("basico", () => { expect(analisarLetraA("Arara Azul")).toEqual([4, 0, 6]); });
  it("nome", () => { expect(analisarLetraA("Mariana")).toEqual([3, 1, 6]); });
  it("semA", () => { expect(analisarLetraA("xyz")).toEqual([0, -1, -1]); });
  it("vazio", () => { expect(analisarLetraA("")).toEqual([0, -1, -1]); });
  it("soA", () => { expect(analisarLetraA("AaA")).toEqual([3, 0, 2]); });
});