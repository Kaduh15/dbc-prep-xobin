import { describe, it, expect } from "vitest";
import { analisarPessoas } from "./solution";

describe("analisarPessoas", () => {
  it.each([
    [[{ nome: "Ana", idade: 30, sexo: "F" }, { nome: "Bruno", idade: 35, sexo: "M" }, { nome: "Carla", idade: 19, sexo: "F" }, { nome: "Diego", idade: 40, sexo: "M" }], [31, "Diego", 1]],
    [[{ nome: "Alice", idade: 25, sexo: "F" }, { nome: "Bob", idade: 20, sexo: "M" }], [22.5, "Bob", 0]],
    [[{ nome: "Ana", idade: 30, sexo: "F" }, { nome: "Bia", idade: 22, sexo: "F" }], [26, "", 0]],
    [[{ nome: "Marina", idade: 18, sexo: "F" }, { nome: "Lucas", idade: 19, sexo: "M" }, { nome: "Pedro", idade: 50, sexo: "M" }], [29, "Pedro", 1]],
    [[{ nome: "Ana", idade: 20, sexo: "F" }, { nome: "Bia", idade: 19, sexo: "F" }], [19.5, "", 1]],
    [[{ nome: "Eva", idade: 30, sexo: "F" }, { nome: "Eva2", idade: 30, sexo: "F" }], [30, "", 0]],
    [[{ nome: "Rui", idade: 22, sexo: "M" }], [22, "Rui", 0]],
    [[{ nome: "Lu", idade: 15, sexo: "F" }, { nome: "Lia", idade: 16, sexo: "F" }], [15.5, "", 2]],
  ])("f(...) -> %j",
    (pessoas, esperado) => {
      expect(analisarPessoas(pessoas)).toEqual(esperado);
    });
  });