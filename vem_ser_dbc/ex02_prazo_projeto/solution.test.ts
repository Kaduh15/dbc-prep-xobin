import { describe, it, expect } from "vitest";
import { prazoProjeto } from "./solution";

describe("prazoProjeto", () => {
  it.each([
    [[["junior"], 10], 1.0],
    [[["junior", "pleno"], 30], 1.0],
    [[[], 100], null],
    [[["senior"], 15], 0.5],
    [[["lider"], 80], 2.0],
    [[["junior", "junior"], 20], 1.0],
    [[["pleno", "senior"], 25], 0.5],
    [[["junior"], 0], 0.0],
])("caso", (args: any, esperado: any) => {
    const resultado = prazoProjeto(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
