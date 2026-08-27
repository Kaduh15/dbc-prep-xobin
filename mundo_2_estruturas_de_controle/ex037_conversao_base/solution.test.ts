import { describe, it, expect } from "vitest";
import { converterBase } from "./solution";

describe("converterBase", () => {
  it("10 em binario", () => {
    expect(converterBase(10, 1)).toEqual("1010");
  });
  it("10 em octal", () => {
    expect(converterBase(10, 2)).toEqual("12");
  });
  it("10 em hexa", () => {
    expect(converterBase(10, 3)).toEqual("a");
  });
  it("255 em binario", () => {
    expect(converterBase(255, 1)).toEqual("11111111");
  });
  it("255 em octal", () => {
    expect(converterBase(255, 2)).toEqual("377");
  });
  it("255 em hexa", () => {
    expect(converterBase(255, 3)).toEqual("ff");
  });
  it("0 em qq base", () => {
    expect(converterBase(0, 2)).toEqual("0");
  });
});
