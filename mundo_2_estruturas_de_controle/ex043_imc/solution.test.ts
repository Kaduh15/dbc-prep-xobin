import { describe, it, expect } from "vitest";
import { calcularImc } from "./solution";

describe("calcularImc", () => {
  it.each([
    [[50, 1.75], "Abaixo do Peso"],
    [[70, 1.75], "Peso Ideal"],
    [[90, 1.75], "Sobrepeso"],
    [[110, 1.75], "Obesidade"],
    [[130, 1.75], "Obesidade Morbida"],
    [[60, 1.75], "Peso Ideal"],
    [[73, 2], "Abaixo do Peso"],
    [[74, 2], "Peso Ideal"],
    [[99, 2], "Peso Ideal"],
    [[100, 2], "Sobrepeso"],
    [[101, 2], "Sobrepeso"],
    [[119, 2], "Sobrepeso"],
    [[120, 2], "Obesidade"],
    [[130, 2], "Obesidade"],
    [[159, 2], "Obesidade"],
    [[160, 2], "Obesidade Morbida"],
    [[200, 2], "Obesidade Morbida"],
  ] as [number[], string][])("caso %#", (args, esperado) => {
    expect(calcularImc(args[0], args[1])).toEqual(esperado);
  });
});
