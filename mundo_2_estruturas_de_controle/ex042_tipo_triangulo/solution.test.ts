import { describe, it, expect } from "vitest";
import { tipoTriangulo } from "./solution";

describe("tipoTriangulo", () => {
  it.each([
    [[2, 2, 2], "equilatero"],
    [[3, 3, 5], "isosceles"],
    [[3, 4, 5], "escaleno"],
    [[1, 1, 3], "invalido"],
    [[10, 2, 3], "invalido"],
    [[3, 3, 3], "equilatero"],
    [[2, 2, 1], "isosceles"],
    [[7, 4, 4], "isosceles"],
    [[5, 4, 3], "escaleno"],
    [[2, 3, 5], "invalido"],
    [[1, 2, 3], "invalido"],
    [[1, 1, 2], "invalido"],
  ] as [number[], string][])("caso %#", (args, esperado) => {
    expect(tipoTriangulo(args[0], args[1], args[2])).toEqual(esperado);
  });
});
