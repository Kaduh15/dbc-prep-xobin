export function anagrama(a: string, b: string): boolean {

  const palavra1 = a.replaceAll(' ', '')
  const palavra2 = b.replaceAll(' ', '')


  if ( palavra1.length !== palavra2.length ) return false
  if (!palavra1 && !palavra2) return true

  
  function ordenaPalavra(palavra: string): string {
    const alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    palavra = palavra.replaceAll(' ', '')

    let indexesDasLetras: number[] = []

    for (let i = 0; i < palavra.length; i++) {

      const letra = palavra[i]

      if (!letra.length) continue

      const indexDaLetra = alfabeto.indexOf(letra)

      indexesDasLetras.push(indexDaLetra)
    }
    
    const indexOrdenadas = indexesDasLetras.sort((a, b) => a - b)

    return indexOrdenadas.toLocaleString()
  }

  return ordenaPalavra(a) === ordenaPalavra(b)
}
