import { describe, it, expect } from "vitest";
import { fizzbuzz } from "./solution";

describe("fizzbuzz", () => {
  it.each([
    [[15], "FizzBuzz"],
    [[3], "Fizz"],
    [[5], "Buzz"],
    [[1], "1"],
    [[30], "FizzBuzz"],
    [[0], "FizzBuzz"],
    [[-3], "Fizz"],
    [[45], "FizzBuzz"],
    [[7], "7"],
])("caso", (args: any[], esperado: any) => {
    const resultado = fizzbuzz(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
