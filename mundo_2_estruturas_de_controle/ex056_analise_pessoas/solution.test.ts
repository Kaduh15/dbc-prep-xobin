import { describe, it, expect } from "vitest";
import { analisarPessoas } from "./solution";

describe("analisarPessoas", () => {
  it.each([
    [
      [
        { nome: "Ana", idade: 30, sexo: "F" },
        { nome: "Bruno", idade: 35, sexo: "M" },
        { nome: "Carla", idade: 19, sexo: "F" },
        { nome: "Diego", idade: 40, sexo: "M" },
      ],
      [31, "Diego", 1],
    ],
    [
      [
        { nome: "Alice", idade: 25, sexo: "F" },
        { nome: "Bob", idade: 20, sexo: "M" },
      ],
      [22.5, "Bob", 0],
    ],
    [
      [
        { nome: "Ana", idade: 30, sexo: "F" },
        { nome: "Bia", idade: 22, sexo: "F" },
      ],
      [26, "", 0],
    ],
  ])("f(%j) -> %j", (pessoas, esperado) => {
    expect(analisarPessoas(pessoas)).toEqual(esperado);
  });
});
