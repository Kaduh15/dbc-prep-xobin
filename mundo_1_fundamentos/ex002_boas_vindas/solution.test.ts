import { describe, it, expect } from "vitest";
import { boasVindas } from "./solution";


describe('boasVindas', () => {
  it.each([
    [["João"], "Olá, João! Seja muito bem-vindo(a)!"],
    [["Maria"], "Olá, Maria! Seja muito bem-vindo(a)!"],
    [[""], "Olá, ! Seja muito bem-vindo(a)!"],
    [["Ana Clara"], "Olá, Ana Clara! Seja muito bem-vindo(a)!"],
    [[" "], "Olá,  ! Seja muito bem-vindo(a)!"],
    [["Zé"], "Olá, Zé! Seja muito bem-vindo(a)!"],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = boasVindas(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
