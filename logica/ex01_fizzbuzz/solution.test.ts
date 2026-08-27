import { describe, it, expect } from "vitest";
import { fizzbuzz } from "./solution";

describe("fizzbuzz", () => {
  it.each([
    [[1], "1"],
    [[3], "Fizz"],
    [[5], "Buzz"],
    [[15], "FizzBuzz"],
    [[9], "Fizz"],
    [[10], "Buzz"],
    [[30], "FizzBuzz"],
    [[7], "7"]
])("caso", (args: any[], esperado: any) => {
    const resultado = fizzbuzz(...(args as []));
    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));
  });
});
