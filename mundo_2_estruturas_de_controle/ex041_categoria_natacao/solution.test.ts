import { describe, it, expect } from "vitest";
import { categoriaNatacao } from "./solution";

describe("categoriaNatacao", () => {
  it.each([
    [[9], "Mirim"],
    [[14], "Infantil"],
    [[17], "Junior"],
    [[19], "Junior"],
    [[20], "Senior"],
    [[25], "Master"],
    [[0], "Mirim"],
    [[5], "Mirim"],
    [[8], "Mirim"],
    [[10], "Infantil"],
    [[15], "Junior"],
    [[21], "Master"],
    [[30], "Master"],
  ] as [number[], string][])("caso %#", (args, esperado) => {
    expect(categoriaNatacao(args[0])).toEqual(esperado);
  });
});
