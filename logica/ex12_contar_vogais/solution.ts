export function contarVogais(texto: string): number {
  const vogais = 'aeiou'

  let contador = 0

  for (let i = 0; i < texto.length; i++) {
    if (vogais.includes(texto[i].toLocaleLowerCase())) contador++
  }

  return contador
}
