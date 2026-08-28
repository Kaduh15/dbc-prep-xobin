#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reforço do lote logica/ (12): expande testes com extremos + enriquece README.
Grava soluções de referência (para validar), testes expandidos e READMEs ricos."""
import os, re, json

BASE = "/home/ubuntu/dbc-prep-xobin/logica"

# ---------- soluções de referência (Python) ----------
def ref_fizzbuzz(n): 
    if n % 15 == 0: return "FizzBuzz"
    if n % 3 == 0: return "Fizz"
    if n % 5 == 0: return "Buzz"
    return str(n)
def ref_palindromo(texto):
    limpo = re.sub(r'[^a-z0-9]', '', texto.lower())
    return limpo == limpo[::-1]
def ref_anagrama(a, b):
    return ''.join(sorted(a.lower().replace(' ', ''))) == ''.join(sorted(b.lower().replace(' ', '')))
def ref_two_sum(nums, alvo):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == alvo: return [i, j]
    return None
def ref_inverter_string(texto): return texto[::-1]
def ref_contar_caracteres(texto):
    d = {}
    for c in texto: d[c] = d.get(c, 0) + 1
    return d
def ref_maior_menor(nums):
    if not nums: return None
    return (max(nums), min(nums))
def ref_soma_digitos(n): return sum(int(c) for c in str(abs(n)))
def ref_fatorial(n):
    r = 1
    for i in range(2, n + 1): r *= i
    return r
def ref_fibonacci(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
def ref_numero_primo(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def ref_contar_vogais(texto): return sum(1 for c in texto.lower() if c in "aeiou")

# ---------- soluções de referência (TypeScript) ----------
TSREF = {
 "fizzbuzz": "export function fizzbuzz(n: number): string {\n  if (n % 15 === 0) return \"FizzBuzz\";\n  if (n % 3 === 0) return \"Fizz\";\n  if (n % 5 === 0) return \"Buzz\";\n  return String(n);\n}\n",
 "palindromo": "export function palindromo(texto: string): boolean {\n  const limpo = texto.toLowerCase().replace(/[^a-z0-9]/g, \"\");\n  return limpo === limpo.split(\"\").reverse().join(\"\");\n}\n",
 "anagrama": "export function anagrama(a: string, b: string): boolean {\n  const ea = a.toLowerCase().replace(/ /g, \"\").split(\"\").sort().join(\"\");\n  const eb = b.toLowerCase().replace(/ /g, \"\").split(\"\").sort().join(\"\");\n  return ea === eb;\n}\n",
 "two_sum": "export function twoSum(nums: number[], alvo: number): number[] | null {\n  for (let i = 0; i < nums.length; i++)\n    for (let j = i + 1; j < nums.length; j++)\n      if (nums[i] + nums[j] === alvo) return [i, j];\n  return null;\n}\n",
 "inverter_string": "export function inverterString(texto: string): string {\n  return texto.split(\"\").reverse().join(\"\");\n}\n",
 "contar_caracteres": "export function contarCaracteres(texto: string): Record<string, number> {\n  const d: Record<string, number> = {};\n  for (const c of texto) d[c] = (d[c] ?? 0) + 1;\n  return d;\n}\n",
 "maior_menor": "export function maiorMenor(nums: number[]): [number, number] | null {\n  if (nums.length === 0) return null;\n  return [Math.max(...nums), Math.min(...nums)];\n}\n",
 "soma_digitos": "export function somaDigitos(n: number): number {\n  return String(Math.abs(n)).split(\"\").reduce((s, c) => s + Number(c), 0);\n}\n",
 "fatorial": "export function fatorial(n: number): number {\n  let r = 1;\n  for (let i = 2; i <= n; i++) r *= i;\n  return r;\n}\n",
 "fibonacci": "export function fibonacci(n: number): number {\n  let a = 0, b = 1;\n  for (let i = 0; i < n; i++) { const t = a + b; a = b; b = t; }\n  return a;\n}\n",
 "numero_primo": "export function numeroPrimo(n: number): boolean {\n  if (n < 2) return false;\n  for (let i = 2; i * i <= n; i++) if (n % i === 0) return false;\n  return true;\n}\n",
 "contar_vogais": "export function contarVogais(texto: string): number {\n  return texto.toLowerCase().split(\"\").filter((c) => \"aeiou\".includes(c)).length;\n}\n",
}

# ---------- casos expandidos: nome -> { args, ref_fn(py) -> esperado } ----------
# cada entrada: (args, ref_nome) — esperado calculado por ref_nome(*args)
CASES = {
 "fizzbuzz": [(15,), (3,), (5,), (1,), (30,), (0,), (-3,), (45,), (7,)],
 "palindromo": [("arara",), ("A man a plan a canal Panama",), ("hello",), ("",), ("Ana",), ("12321",), ("a",), ("ab",)],
 "anagrama": [("listen","silent"), ("triangle","integral"), ("cat","dog"), ("hello","hello"), ("",""), ("a","b"), ("anagram","nag a ram"), ("python","java")],
 "two_sum": [([2,7,11,15],9), ([3,2,4],6), ([3,3],6), ([],5), ([1,2,3],99), ([-1,-2,-3],-3), ([0,0,1],0), ([5,5,5],10), ([1],1)],
 "inverter_string": [("hello",), ("",), ("abc",), ("a",), ("a man",), ("olá mundo",)],
 "contar_caracteres": [("banana",), ("",), ("a",), ("ab a",), ("aba",)],
 "maior_menor": [([3,1,4,1,5],), ([],), ([7],), ([-1,-5,-3],), ([0,0],), ([100,5,200],)],
 "soma_digitos": [(123,), (0,), (-45,), (9,), (1000,), (7,)],
 "fatorial": [(0,), (1,), (5,), (3,), (2,), (6,)],
 "fibonacci": [(0,), (1,), (2,), (5,), (10,), (6,)],
 "numero_primo": [(0,), (1,), (2,), (3,), (4,), (9,), (97,), (25,)],
 "contar_vogais": [("hello",), ("",), ("AEIOU",), ("try",), ("banana",), ("Olá",)],
}

REF = {
 "fizzbuzz": ref_fizzbuzz, "palindromo": ref_palindromo, "anagrama": ref_anagrama,
 "two_sum": ref_two_sum, "inverter_string": ref_inverter_string,
 "contar_caracteres": ref_contar_caracteres, "maior_menor": ref_maior_menor,
 "soma_digitos": ref_soma_digitos, "fatorial": ref_fatorial, "fibonacci": ref_fibonacci,
 "numero_primo": ref_numero_primo, "contar_vogais": ref_contar_vogais,
}

DESC = {
 "fizzbuzz": ("FizzBuzz", "Dado um inteiro n, retorne \"FizzBuzz\" se for múltiplo de 15, \"Fizz\" se múltiplo de 3, \"Buzz\" se múltiplo de 5; caso contrário, o número como string.",
   "Cheque a divisibilidade na ordem 15 → 3 → 5 → número. O módulo % captura os múltiplos; a ordem importa para não mascarar o FizzBuzz."),
 "palindromo": ("Palíndromo", "Dada uma string, retorne True se ela for um palíndromo, ignorando maiúsculas, espaços e pontuação (só letras a-z e dígitos 0-9 contam).",
   "Normalize (lowercase + remova tudo que não for a-z/0-9) e compare a string com sua inversão. É simétrico por construção."),
 "anagrama": ("Anagrama", "Dadas duas strings, retorne True se uma for um anagrama da outra (mesmas letras, ignorando espaços e caixa).",
   "Ordene as letras (após remover espaços e minúsculas) e compare: anagramas têm o mesmo multiconjunto de caracteres."),
 "two_sum": ("Two Sum", "Dada uma lista de inteiros nums e um alvo, retorne os índices [i, j] com i<j do PRIMEIRO par cuja soma é o alvo; None/[] se não houver.",
   "Força bruta O(n²) com dois laços é o suficiente; para O(n) use um dicionário guardando o complemento esperado visto."),
 "inverter_string": ("Inverter String", "Dada uma string, retorne a versão invertida.",
   "Itere do fim para o início concatenando (Python [::-1]; TS split/reverse/join). Simples e determinístico."),
 "contar_caracteres": ("Contar Caracteres", "Dada uma string, retorne um dicionário/mapa contando quantas vezes cada caractere aparece (espaços e pontuação contam).",
   "Itere e incremente um acumulador por caractere (d.get em Python; ?? em TS)."),
 "maior_menor": ("Maior e Menor", "Dada uma lista de números, retorne a tupla/array (maior, menor). Para lista vazia, retorne None/null.",
   "Varrer uma vez mantendo max e min; trate o caso vazio antes."),
 "soma_digitos": ("Soma dos Dígitos", "Dado um inteiro, retorne a soma dos dígitos do seu valor absoluto.",
   "Tome o valor absoluto, converta para string e some cada caractere como dígito. Negativos usam a magnitude."),
 "fatorial": ("Fatorial", "Dado um inteiro n ≥ 0, retorne n! (produto 1×2×…×n, com 0! = 1).",
   "Produto acumulado de 1 a n; defina o caso-base 0! = 1."),
 "fibonacci": ("Fibonacci", "Dado um inteiro n ≥ 0, retorne o n-ésimo termo da sequência de Fibonacci (F0=0, F1=1).",
   "Itere atualizando (a,b) = (b, a+b); F_n é o valor após n passos."),
 "numero_primo": ("Número Primo", "Dado um inteiro, retorne True se for primo (divisível só por 1 e por ele mesmo).",
   "Números < 2 não são primos; teste divisores até √n — se algum dividir, não é primo."),
 "contar_vogais": ("Contar Vogais", "Dada uma string, retorne quantas vogais (a, e, i, o, u) ela tem, ignorando maiúsculas.",
   "Baixe tudo para minúsculas e conte os caracteres que estão no conjunto \"aeiou\"."),
}

ORDER = ["fizzbuzz","palindromo","anagrama","two_sum","inverter_string","contar_caracteres",
         "maior_menor","soma_digitos","fatorial","fibonacci","numero_primo","contar_vogais"]
FOLDER = {n: f"ex{i+1:02d}_{n}" for i, n in enumerate(ORDER)}
PYNAME = {"two_sum":"two_sum","maior_menor":"maior_menor","contar_caracteres":"contar_caracteres"}
TSNAME = {"two_sum":"twoSum","inverter_string":"inverterString","contar_caracteres":"contarCaracteres","maior_menor":"maiorMenor","soma_digitos":"somaDigitos","numero_primo":"numeroPrimo","contar_vogais":"contarVogais"}

SIG = {
 "fizzbuzz": ("def fizzbuzz(n: int) -> str:", "export function fizzbuzz(n: number): string {"),
 "palindromo": ("def palindromo(texto: str) -> bool:", "export function palindromo(texto: string): boolean {"),
 "anagrama": ("def anagrama(a: str, b: str) -> bool:", "export function anagrama(a: string, b: string): boolean {"),
 "two_sum": ("def two_sum(nums: list, alvo: int) -> list | None:", "export function twoSum(nums: number[], alvo: number): number[] | null {"),
 "inverter_string": ("def inverter_string(texto: str) -> str:", "export function inverterString(texto: string): string {"),
 "contar_caracteres": ("def contar_caracteres(texto: str) -> dict:", "export function contarCaracteres(texto: string): Record<string, number> {"),
 "maior_menor": ("def maior_menor(nums: list) -> tuple | None:", "export function maiorMenor(nums: number[]): [number, number] | null {"),
 "soma_digitos": ("def soma_digitos(n: int) -> int:", "export function somaDigitos(n: number): number {"),
 "fatorial": ("def fatorial(n: int) -> int:", "export function fatorial(n: number): number {"),
 "fibonacci": ("def fibonacci(n: int) -> int:", "export function fibonacci(n: number): number {"),
 "numero_primo": ("def numero_primo(n: int) -> bool:", "export function numeroPrimo(n: number): boolean {"),
 "contar_vogais": ("def contar_vogais(texto: str) -> int:", "export function contarVogais(texto: string): number {"),
}

def tsval(v):
    if v is None: return "null"
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, tuple): return "[" + ", ".join(tsval(x) for x in v) + "]"
    if isinstance(v, list): return "[" + ", ".join(tsval(x) for x in v) + "]"
    if isinstance(v, dict): return "{" + ", ".join(f"{json.dumps(str(k))}: {tsval(val)}" for k, val in v.items()) + "}"
    if isinstance(v, str): return json.dumps(v)
    return str(v)

def format_py_case(args, exp):
    a = repr(tuple(args))
    e = repr(exp)
    return f"    ({a}, {e}),"

def format_ts_case(args, exp):
    a = "[" + ", ".join(tsval(x) for x in args) + "]"
    e = tsval(exp)
    return f"    [{a}, {e}],"

def build_pytest(name):
    stub = f"solution_{FOLDER[name]}"
    imported = "two_sum" if name == "two_sum" else name
    lines = [f"from {stub} import {imported}", "import pytest", "", ""]
    lines.append("@pytest.mark.parametrize(\"args,esperado\", [")
    for args in CASES[name]:
        exp = REF[name](*args)
        lines.append(format_py_case(args, exp))
    lines.append("])")
    lines.append("def test_caso(args, esperado):")
    lines.append("    assert " + name + "(*args) == esperado")
    return "\n".join(lines) + "\n"

def build_vitest(name):
    fn = TSNAME.get(name, name)
    lines = ["import { describe, it, expect } from \"vitest\";", f"import {{ {fn} }} from \"./solution\";", ""]
    lines.append(f"describe(\"{fn}\", () => {{")
    lines.append("  it.each([")
    for args in CASES[name]:
        exp = REF[name](*args)
        lines.append(format_ts_case(args, exp))
    lines.append("])(\"caso\", (args: any[], esperado: any) => {")
    lines.append(f"    const resultado = {fn}(...(args as []));")
    lines.append("    expect(JSON.stringify(resultado)).toBe(JSON.stringify(esperado));")
    lines.append("  });")
    lines.append("});")
    return "\n".join(lines) + "\n"

def build_readme(name):
    title, desc, dica = DESC[name]
    py_sig, ts_sig = SIG[name]
    # extremos explícitos para documentar
    edges = {
     "fizzbuzz": "Múltiplo exato (0, 15, 30, 45); múltiplo só de 3 ou só de 5; números negativos (ex.: -3 é Fizz); números não múltiplos.",
     "palindromo": "String vazia (é palíndromo); um único caractere; palíndromo com espaços/pontuação; dígitos; caixa mista (Ana/ana); string não simétrica.",
     "anagrama": "Duas strings vazias (são anagramas); strings iguais; comprimentos diferentes; espaços no meio de um dos lados; uma letra vs outra.",
     "two_sum": "Lista vazia e com um único elemento (sem par → None); alvo com negativos; zeros/duplicados (0+0 e 5+5); sem par possível; par no começo da lista.",
     "inverter_string": "String vazia; um único caractere; acentos/unicode („olá mundo“); espaços; inversão que muda a ordem das palavras.",
     "contar_caracteres": "String vazia (retorna {}); um único caractere; espaços e símbolos contam; caracteres repetidos; todos iguais.",
     "maior_menor": "Lista vazia (None/null); um único elemento (maior=menor); negativos; zeros repetidos; valores grandes/pequenos na mesma lista.",
     "soma_digitos": "Zero (soma 0); dígito único; números negativos (usa valor absoluto); com zeros internos (1000); dezenas/hábitos comuns.",
     "fatorial": "0! = 1 (caso-base); 1! = 1; números pequenos (2,3,5); fatoriais intermediários (6!=720).",
     "fibonacci": "F0=0; F1=1; termos iniciais (2,5,6); um termo de meio (ex.: F10=55) para conferir a enumeração a partir de 0.",
     "numero_primo": "0 e 1 (não primos); 2 e 3 (primos); quadrados perfeitos (4, 9, 25 → não primos); primo grande (97); composto ímpar (9).",
     "contar_vogais": "String vazia (0); sem vogais (consoantes); maiúsculas (AEIOU); vogais repetidas (banana); acentos não contam (á ≠ a).",
    }
    with open(f"{BASE}/{FOLDER[name]}/README.md", "r") as f:
        cur = f.read()
    # preserva a assinatura original se já existir (extrai seção), senão usa SIG
    sig_py, sig_ts = SIG[name]

    c = []
    num = FOLDER[name].split("_")[0][2:]  # ex.: "01"
    c.append(f"# Exercício {num} — {title}")
    c.append("")
    c.append("## Descrição do Problema")
    c.append(desc)
    c.append("")
    c.append("## Parâmetros e Tipos Esperados")
    line = ASC[name]
    c.append(line)
    c.append("")
    c.append("## Formato do Retorno")
    c.append(RET[name])
    c.append("")
    c.append("## Casos de Exemplo")
    c.append("```python")
    c.append("# (args) -> esperado")
    for args in CASES[name][:5]:
        c.append(format_py_case(args, REF[name](*args)))
    c.append("```")
    c.append("")
    c.append("## Casos de Teste (todos, incluindo extremos)")
    c.append("```python")
    for args in CASES[name]:
        c.append(format_py_case(args, REF[name](*args)))
    c.append("```")
    c.append("")
    c.append("## Edge Cases / Extremos")
    c.append(edges[name])
    c.append("")
    c.append("## Abordagem / Dica")
    c.append(dica)
    c.append("")
    c.append("## Complexidade")
    c.append(COMP[name])
    c.append("")
    c.append("## Assinatura Canônica")
    c.append(f"- **Python**: `{sig_py}`")
    c.append(f"- **TypeScript**: `{sig_ts}`")
    c.append("")
    c.append(f"> Stub para editar: `{FOLDER[name]}/solution_{FOLDER[name]}.py` (Python) e `solution.ts` (TS).")
    c.append("")
    return "\n".join(c) + "\n"

ASC = {
 "fizzbuzz": "- n: int",
 "palindromo": "- texto: str",
 "anagrama": "- a: str, b: str",
 "two_sum": "- nums: list[int], alvo: int",
 "inverter_string": "- texto: str",
 "contar_caracteres": "- texto: str",
 "maior_menor": "- nums: list[int]",
 "soma_digitos": "- n: int",
 "fatorial": "- n: int (n >= 0)",
 "fibonacci": "- n: int (n >= 0)",
 "numero_primo": "- n: int",
 "contar_vogais": "- texto: str",
}
RET = {
 "fizzbuzz": "- str: \"FizzBuzz\" | \"Fizz\" | \"Buzz\" | o número como string",
 "palindromo": "- bool: True se palíndromo",
 "anagrama": "- bool: True se são anagramas",
 "two_sum": "- list[int] (2 índices) ou None",
 "inverter_string": "- str: string invertida",
 "contar_caracteres": "- dict: {caractere: contagem}",
 "maior_menor": "- tuple[int, int] (maior, menor) ou None",
 "soma_digitos": "- int: soma dos dígitos de |n|",
 "fatorial": "- int: n!",
 "fibonacci": "- int: F_n (F0=0)",
 "numero_primo": "- bool: True se primo",
 "contar_vogais": "- int: quantidade de vogais",
}
COMP = {
 "fizzbuzz": "- Tempo O(1), espaço O(1)",
 "palindromo": "- Tempo O(n), espaço O(n)",
 "anagrama": "- Tempo O(a·log a + b·log b) com ordenação, espaço O(a+b)",
 "two_sum": "- Tempo O(n²) força bruta / O(n) com hash, espaço O(1) / O(n)",
 "inverter_string": "- Tempo O(n), espaço O(n)",
 "contar_caracteres": "- Tempo O(n), espaço O(k) (k = caracteres distintos)",
 "maior_menor": "- Tempo O(n), espaço O(1)",
 "soma_digitos": "- Tempo O(log n), espaço O(log n)",
 "fatorial": "- Tempo O(n), espaço O(1)",
 "fibonacci": "- Tempo O(n), espaço O(1)",
 "numero_primo": "- Tempo O(√n), espaço O(1)",
 "contar_vogais": "- Tempo O(n), espaço O(1)",
}

# código-fonte das soluções de referência (Python)
PYREF = {
 "fizzbuzz": '''def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
''',
 "palindromo": '''import re

def palindromo(texto: str) -> bool:
    limpo = re.sub(r"[^a-z0-9]", "", texto.lower())
    return limpo == limpo[::-1]
''',
 "anagrama": '''def anagrama(a: str, b: str) -> bool:
    ea = "".join(sorted(a.lower().replace(" ", "")))
    eb = "".join(sorted(b.lower().replace(" ", "")))
    return ea == eb
''',
 "two_sum": '''def two_sum(nums: list, alvo: int) -> list | None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == alvo:
                return [i, j]
    return None
''',
 "inverter_string": '''def inverter_string(texto: str) -> str:
    return texto[::-1]
''',
 "contar_caracteres": '''def contar_caracteres(texto: str) -> dict:
    d = {}
    for c in texto:
        d[c] = d.get(c, 0) + 1
    return d
''',
 "maior_menor": '''def maior_menor(nums: list) -> tuple | None:
    if not nums:
        return None
    return (max(nums), min(nums))
''',
 "soma_digitos": '''def soma_digitos(n: int) -> int:
    return sum(int(c) for c in str(abs(n)))
''',
 "fatorial": '''def fatorial(n: int) -> int:
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r
''',
 "fibonacci": '''def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
''',
 "numero_primo": '''def numero_primo(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
''',
 "contar_vogais": '''def contar_vogais(texto: str) -> int:
    return sum(1 for c in texto.lower() if c in "aeiou")
''',
}

def build_solution_py(name):
    return PYREF[name]

# grava solução de referência + testes expandidos + README
for name in ORDER:
    d = f"{BASE}/{FOLDER[name]}"
    open(f"{d}/solution_{FOLDER[name]}.py", "w").write(build_solution_py(name))
    open(f"{d}/solution.ts", "w").write(TSREF[name])
    open(f"{d}/test_{FOLDER[name]}.py", "w").write(build_pytest(name))
    open(f"{d}/solution.test.ts", "w").write(build_vitest(name))
    open(f"{d}/README.md", "w").write(build_readme(name))
    if os.path.exists(f"{d}/solution.py"):
        os.remove(f"{d}/solution.py")
    print("ok", FOLDER[name])

# ===== restaura stubs de TDD (após validação) =====
for name in ORDER:
    d = f"{BASE}/{FOLDER[name]}"
    py_sig, ts_sig = SIG[name]
    stub_py = py_sig + "\n    raise NotImplementedError\n"
    stub_ts = ts_sig + "\n  throw new Error(\"Not implemented\");\n}\n"
    open(f"{d}/solution_{FOLDER[name]}.py", "w").write(stub_py)
    open(f"{d}/solution.ts", "w").write(stub_ts)
print("stubs restaurados (TDD).")

print("gerado. rodar pytest e vitest para validar.")