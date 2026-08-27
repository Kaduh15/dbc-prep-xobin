import { describe, it, expect } from "vitest";
import { tipoTriangulo } from "./solution";

describe("tipoTriangulo", () => {
  it('tipoTriangulo(2, 2, 2)', () => {
    expect(tipoTriangulo(2, 2, 2)).toEqual('equilatero');
  });
  it('tipoTriangulo(3, 3, 5)', () => {
    expect(tipoTriangulo(3, 3, 5)).toEqual('isosceles');
  });
  it('tipoTriangulo(3, 4, 5)', () => {
    expect(tipoTriangulo(3, 4, 5)).toEqual('escaleno');
  });
  it('tipoTriangulo(1, 1, 3)', () => {
    expect(tipoTriangulo(1, 1, 3)).toEqual('invalido');
  });
  it('tipoTriangulo(10, 2, 3)', () => {
    expect(tipoTriangulo(10, 2, 3)).toEqual('invalido');
  });
});
