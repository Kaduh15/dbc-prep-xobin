import { describe, it, expect } from "vitest";
import { formaTriangulo } from "./solution";

describe("formaTriangulo", () => {
  it("valido", () => { expect(formaTriangulo(3, 4, 5)).toBe(true); });
  it("degenerado", () => { expect(formaTriangulo(1, 2, 3)).toBe(false); });
  it("ladoGrande", () => { expect(formaTriangulo(10, 1, 1)).toBe(false); });
  it("equilatero", () => { expect(formaTriangulo(5.5, 5.5, 5.5)).toBe(true); });
  it("impossivel", () => { expect(formaTriangulo(7, 2, 4)).toBe(false); });
  it("limite", () => { expect(formaTriangulo(2, 3, 4)).toBe(true); });
});