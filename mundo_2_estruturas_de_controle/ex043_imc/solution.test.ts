import { describe, it, expect } from "vitest";
import { calcularImc } from "./solution";

describe("calcularImc", () => {
  it('calcularImc(50, 1.75)', () => {
    expect(calcularImc(50, 1.75)).toEqual('Abaixo do Peso');
  });
  it('calcularImc(70, 1.75)', () => {
    expect(calcularImc(70, 1.75)).toEqual('Peso Ideal');
  });
  it('calcularImc(90, 1.75)', () => {
    expect(calcularImc(90, 1.75)).toEqual('Sobrepeso');
  });
  it('calcularImc(110, 1.75)', () => {
    expect(calcularImc(110, 1.75)).toEqual('Obesidade');
  });
  it('calcularImc(130, 1.75)', () => {
    expect(calcularImc(130, 1.75)).toEqual('Obesidade Morbida');
  });
  it('calcularImc(60, 1.75)', () => {
    expect(calcularImc(60, 1.75)).toEqual('Peso Ideal');
  });
});
