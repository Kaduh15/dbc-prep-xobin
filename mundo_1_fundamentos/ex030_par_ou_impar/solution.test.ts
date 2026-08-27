import { describe, it, expect } from "vitest";
import { parOuImpar } from "./solution";

describe("parOuImpar", () => {
  it("par", () => { expect(parOuImpar(2)).toBe("PAR"); });
  it("impar", () => { expect(parOuImpar(3)).toBe("\u00cdMPAR"); });
  it("zero", () => { expect(parOuImpar(0)).toBe("PAR"); });
  it("negPar", () => { expect(parOuImpar(-4)).toBe("PAR"); });
  it("negImpar", () => { expect(parOuImpar(-7)).toBe("\u00cdMPAR"); });
});
