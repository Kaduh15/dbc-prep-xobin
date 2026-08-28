export function fibonacci(n: number): number {
  if (n === 0) return 0

  let resultado = 0
  let ultimoResultado = 0

  for (let i = 1; i <= n; i++) {
    if (i === 1) ultimoResultado = i

    const salvaResultado = resultado
    
    resultado += ultimoResultado

    ultimoResultado = salvaResultado
  }

  return resultado
}
