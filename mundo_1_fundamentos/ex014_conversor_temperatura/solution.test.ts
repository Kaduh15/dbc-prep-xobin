import { describe, expect, it } from "vitest";
import { celsiusParaFahrenheit } from "./solution";

describe("celsiusParaFahrenheit", () => {
  it.each([
    [0, 32.0],
    [100, 212.0],
    [-40, -40.0],
    [37, 98.6],
    [25, 77.0],
  ])("celsiusParaFahrenheit(%d) retorna %d", (celsius, esperado) => {
    expect(celsiusParaFahrenheit(celsius)).toBeCloseTo(esperado, 10);
  });
});