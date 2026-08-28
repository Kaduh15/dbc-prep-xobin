export function numeroPrimo(n: number): boolean {
  if(n <= 1) return false

  let divisores = 0

  for (let i = 1; i <= 10; i++){
    if (n % i === 0) divisores += 1

    if (divisores > 2) return false
    if (n > 10 && divisores >= 2) return false
  }


  return true
}
 