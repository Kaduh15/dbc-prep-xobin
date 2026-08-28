export function fatorial(n: number): number {
  if ( n === 0 ) return 1

  let fatorial = 1

  for (let i = 1; i <=n; i++) {
    fatorial *= i
  }

  return fatorial
}
