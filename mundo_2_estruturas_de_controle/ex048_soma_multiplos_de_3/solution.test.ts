import { describe, it, expect } from "vitest";
import { somaMultiplosDe3 } from "./solution";

describe("somaMultiplosDe3", () => {
  it('somaMultiplosDe3()', () => {
    expect(somaMultiplosDe3()).toEqual(41583);
  });
  it('somaMultiplosDe3(1, 10)', () => {
    expect(somaMultiplosDe3(1, 10)).toEqual(18);
  });
  it('somaMultiplosDe3(5, 12)', () => {
    expect(somaMultiplosDe3(5, 12)).toEqual(27);
  });
  it('somaMultiplosDe3(1, 6)', () => {
    expect(somaMultiplosDe3(1, 6)).toEqual(9);
  });
  it('somaMultiplosDe3(3, 3)', () => {
    expect(somaMultiplosDe3(3, 3)).toEqual(3);
  });
});
