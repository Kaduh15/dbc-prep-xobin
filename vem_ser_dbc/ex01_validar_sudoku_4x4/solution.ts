export function validarSudoku4x4(grid: number[][]): boolean {
  if (grid.length !== 4) return false
  if (grid.some((linha) => linha.length !== 4)) return false

  function checarLinhas(g: number[][]): boolean {
    const setMap = new Set<Number>()

    let resultado: boolean = true

    for (const linha of g) {

      console.log(linha)

      linha.forEach((numero) => {
        if (setMap.has(numero) || numero > 4 || numero < 1) {
          resultado = false
          return
        }

        setMap.add(numero)
      })

      setMap.clear()
    }

    return resultado
  }

  function checarColunas(g: number[][]): boolean {
    const mapColunas = g.map((_, i) => {
      return [g[0][i], g[1][i], g[2][i], g[3][i]]
    })

    return checarLinhas(mapColunas)
  }


  console.log("=========== LINHAS ===========")
  console.log(checarLinhas([
    [1, 1, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1]
  ]))

  console.log("=========== COLUNAS ===========")
  console.log(checarColunas([
    [1, 1, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1]
  ]))


  return checarLinhas(grid) && checarColunas(grid)
}
