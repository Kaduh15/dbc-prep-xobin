import { describe, it, expect } from "vitest";
import { situacaoAlistamento } from "./solution";

describe("situacaoAlistamento", () => {
  it.each([
    [[16], "faltam 2 anos"],
    [[17], "faltam 1 ano"],
    [[18], "hora de se alistar"],
    [[21], "ja passou 3 anos"],
    [[30], "ja passou 12 anos"],
    [[0], "faltam 18 anos"],
    [[1], "faltam 17 anos"],
    [[19], "ja passou 1 ano"],
    [[25], "ja passou 7 anos"],
    [[100], "ja passou 82 anos"],
  ] as [number[], string][])("caso %#", (args, esperado) => {
    expect(situacaoAlistamento(args[0])).toEqual(esperado);
  });
});
