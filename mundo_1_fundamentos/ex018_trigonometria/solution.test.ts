import { describe, expect, it } from "vitest";
import { trigonometria } from "./solution";

describe("trigonometria", () => {
  it.each([[0, [0.0, 1.0, 0.0]],
    [30, [0.5, 0.8660254037844386, 0.5773502691896257]],
    [45, [0.7071067811865475, 0.7071067811865475, 1.0]],
    [60, [0.8660254037844386, 0.5, 1.7320508075688767]],
    [180, [0.0, -1.0, 0.0]],
    [22.5, [0.3826834323650898, 0.9238795325112867, 0.41421356237309503]]])
    ("trigonometria(%d) retorna [%d, %d, %d]", (angulo, esperado) => {
    const [s, c, t] = trigonometria(angulo);
    expect(s).toBeCloseTo(esperado[0], 10);
    expect(c).toBeCloseTo(esperado[1], 10);
    expect(t).toBeCloseTo(esperado[2], 10);
  });
});
