import { describe, it, expect } from "vitest";
import { converterBase } from "./solution";

describe("converterBase", () => {
  it.each([
    [[10, 1], "1010"],
    [[10, 2], "12"],
    [[10, 3], "a"],
    [[255, 1], "11111111"],
    [[255, 2], "377"],
    [[255, 3], "ff"],
    [[0, 2], "0"],
    [[0, 1], "0"],
    [[0, 3], "0"],
    [[16, 1], "10000"],
    [[16, 3], "10"],
    [[31, 1], "11111"],
    [[8, 2], "10"],
    [[1000, 3], "3e8"],
  ] as [number[], string][])("caso %#", (args, esperado) => {
    expect(converterBase(args[0], args[1])).toEqual(esperado);
  });

  it("base invalida lanca", () => {
    expect(() => converterBase(10, 9)).toThrow();
    expect(() => converterBase(10, 0)).toThrow();
  });
});
