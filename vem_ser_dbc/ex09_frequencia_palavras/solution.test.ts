import { describe, it, expect } from "vitest";
import { frequenciaPalavras } from "./solution";

describe("frequenciaPalavras", () => {
  it.each([
    [[""], {}],
    [["ola ola"], {"ola": 2}],
    [["Ola OLA ola"], {"ola": 3}],
    [["casa, jardim! casa."], {"casa": 2, "jardim": 1}],
    [["a b c"], {"a": 1, "b": 1, "c": 1}],
    [["ol\u00e1 mundo, ol\u00e1"], {"ol\u00e1": 2, "mundo": 1}],
])("caso", (args: any, esperado: any) => {
    const resultado = frequenciaPalavras(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
