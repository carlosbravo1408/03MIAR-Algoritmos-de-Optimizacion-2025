from typing import List, Tuple, Optional

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.colors import ListedColormap


def draw_board(
        solution: List[int],
        color_board: Tuple[str, str] = ('#FFCE9E', '#D18B47'),
        ax: Optional[Axes] = None,
) -> Axes:
    """
    - Autor: Carlos Javier Bravo Intriago
    - Fecha: Enero 2026
    -----------------------

    Método que permite dibujar el tablero de ajedrez a la solución definida
    en `solution` para el problema de las N-Reinas.
    Este código fue parte de otro proyecto personal y ha sido reescrito para
    representar las posiciones de las reinas.
    Permite resultados `zero-index` o `one-index`.
    Utiliza recursos sencillos de matplotlib

    -----------------------


    :param solution: Lista con la solución base al modelo [R1, R2, R3, ...,
           RN] donde cada posición corresponde a su columna, y cada elemento
           interno corresponde a la fila
    :param color_board: para poder definir el color del tablero, por defecto
           esta el formato de Lichess.com
    :param ax: Este parametro es opcional, permite agregar este subplot a
           alguna grafica mas compleja.
    :return: Axes: Retorna el objeto Axes de la figura (Basándose en el
             Estándar propuesto por Seaborn o Matplotlib)
    """
    n = len(solution)
    starts_with_one = not 0 in solution
    X, Y = np.meshgrid(np.arange(n), np.arange(n))
    board = (X + Y) % 2

    # Seaborn and Matplotlib ecosystem-friendly allows to easily compose complex figures (such as subplots).
    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))

    cmap = ListedColormap(list(color_board))
    ax.imshow(board, cmap=cmap, origin='lower', extent=(0, n, 0, n))

    for col, row in enumerate(solution):
        ax.text(
            col + 0.5 ,
            row + 0.5 - (1 if starts_with_one else 0),
            '♛',
            fontsize=250/n,
            ha='center', va='center',
            color="black"
        )
    # hacky trick for enable horizontal and vertical ticks when ax is defined
    # No reference for this hardcoded part, I only found it through trial and error
    # Carlos Javier Bravo Intriago
    ax.set_xticks(np.arange(0, n, 1))
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_xticks(np.arange(0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(0.5, n, 1), minor=True)

    ax.set_xticklabels([chr(i + 65) for i in range(n)], minor=True)
    ax.set_yticklabels(np.arange(1,n+1), minor=True)
    ax.tick_params(axis='both', which='major', length=0, labelbottom=False, labelleft=False)
    ax.set_title(f"N={n}: Solución {solution}", fontsize=10)
    ax.grid(False)
    return ax
