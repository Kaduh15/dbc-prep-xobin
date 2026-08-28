import { describe, it, expect } from "vitest";
import { analisarValor } from "./solution";


describe('analisarValor', () => {
  it.each([
    [["Python"], {tipo: 'str', so_espacos: false, e_numero: false, e_alfabetico: true, e_alfanumerico: true, em_maiusculas: false, em_minusculas: false, capitalizada: true}],
    [["1234"], {tipo: 'str', so_espacos: false, e_numero: true, e_alfabetico: false, e_alfanumerico: true, em_maiusculas: false, em_minusculas: false, capitalizada: false}],
    [["   "], {tipo: 'str', so_espacos: true, e_numero: false, e_alfabetico: false, e_alfanumerico: false, em_maiusculas: false, em_minusculas: false, capitalizada: false}],
    [[""], {tipo: 'str', so_espacos: false, e_numero: false, e_alfabetico: false, e_alfanumerico: false, em_maiusculas: false, em_minusculas: false, capitalizada: false}],
    [["ABC"], {tipo: 'str', so_espacos: false, e_numero: false, e_alfabetico: true, e_alfanumerico: true, em_maiusculas: true, em_minusculas: false, capitalizada: false}],
    [["abc"], {tipo: 'str', so_espacos: false, e_numero: false, e_alfabetico: true, e_alfanumerico: true, em_maiusculas: false, em_minusculas: true, capitalizada: false}],
    [["Hello World"], {tipo: 'str', so_espacos: false, e_numero: false, e_alfabetico: false, e_alfanumerico: false, em_maiusculas: false, em_minusculas: false, capitalizada: true}],
    [["12A"], {tipo: 'str', so_espacos: false, e_numero: false, e_alfabetico: false, e_alfanumerico: true, em_maiusculas: true, em_minusculas: false, capitalizada: true}],
    [["123abc"], {tipo: 'str', so_espacos: false, e_numero: false, e_alfabetico: false, e_alfanumerico: true, em_maiusculas: false, em_minusculas: true, capitalizada: false}],
    [["   X"], {tipo: 'str', so_espacos: false, e_numero: false, e_alfabetico: false, e_alfanumerico: false, em_maiusculas: true, em_minusculas: false, capitalizada: true}],
  ])("caso", (args: any[], esperado: any) => {
    const resultado = analisarValor(...(args as []));
    expect(resultado).toEqual(esperado);
  });
});
