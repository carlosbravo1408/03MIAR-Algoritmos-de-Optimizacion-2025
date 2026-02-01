from typing import List, Any, Optional


SolutionType = List[int]
PathsType = List[List[Any]]


# Recuperado de: https://stackoverflow.com/a/28938235
class ConsoleColors:
    # Reset
    Color_Off = '\033[0m'  # Text Reset

    # Regular Colors
    Black = '\033[30m'  # Black
    Red = '\033[31m'  # Red
    Green = '\033[32m'  # Green
    Yellow = '\033[33m'  # Yellow
    Blue = '\033[34m'  # Blue
    Magenta = '\033[35m'  # Magenta
    Cyan = '\033[36m'  # Cyan
    White = '\033[37m'  # White

    # Background
    On_Black = '\033[40m'  # Black
    On_Red = '\033[41m'  # Red
    On_Green = '\033[42m'  # Green
    On_Yellow = '\033[43m'  # Yellow
    On_Blue = '\033[44m'  # Blue
    On_Magenta = '\033[45m'  # Magenta
    On_Cyan = '\033[46m'  # Cyan
    On_White = '\033[47m'  # White


def print_matrix(
        matrix: PathsType,
        *solutions: SolutionType,
        title: Optional[str] = None,
        width: int = 6,
        enable_headers: bool = True,
        header_row_char: str = "",
        header_col_char: str = "",
) -> None:

    RESET = ConsoleColors.Color_Off
    TEXT_WHITE = ConsoleColors.Black
    BG_LEFT = ConsoleColors.On_Cyan
    BG_RIGHT = ConsoleColors.On_Magenta

    if len(header_row_char) > 1: header_row_char = header_row_char[0]
    if len(header_col_char) > 1: header_col_char = header_col_char[0]

    matrix_width = len(matrix) * width
    total_width = matrix_width + (5 if enable_headers else 0)

    if title:
        print(f"{title:^{total_width}}")

    if len(solutions) > 0:
        legend_parts = ["Leyenda:", f"{BG_LEFT}{TEXT_WHITE} Sol 1 {RESET}"]
        if len(solutions) > 1:
            legend_parts.append(f"{BG_RIGHT}{TEXT_WHITE} Sol 2 {RESET}")
            legend_parts.append(
                f"{BG_LEFT}{TEXT_WHITE}  Am{BG_RIGHT}bos {RESET}")
        print(" ".join(legend_parts))

    if title or len(solutions) > 0:
        if enable_headers: print("-" * 5, end="")
        print("-" * matrix_width)
        if enable_headers:
            print(" " * 5, end="")
            for j in range(len(matrix[0])):
                h = f"{header_col_char}{j}"
                print(f"{h:>{width}}", end="")
            print()
            print("    " + "-" * (matrix_width + 1))

        for i, row in enumerate(matrix):
            if enable_headers:
                h = f"{header_row_char}{i}"
                print(f"{h:>{3}} |", end="")

            row_str_parts = []
            for j, val in enumerate(row):
                val_str = str(val).replace('inf', '∞')
                formatted_cell = f"{val_str:>{width}}"
                in_s1 = False
                in_s2 = False

                if len(solutions) > 0:
                    if i < len(solutions[0]) and solutions[0][i] == j:
                        in_s1 = True
                if len(solutions) > 1:
                    if i < len(solutions[1]) and solutions[1][i] == j:
                        in_s2 = True
                cell_content = formatted_cell  # Default
                if in_s1 and in_s2:
                    mid = width // 2
                    cell_content = (
                        f"{BG_LEFT}{TEXT_WHITE}{formatted_cell[:mid]}"
                        f"{BG_RIGHT}{TEXT_WHITE}{formatted_cell[mid:]}"
                        f"{RESET}"
                    )
                elif in_s1:
                    cell_content = f"{BG_LEFT}{TEXT_WHITE}{formatted_cell}{RESET}"
                elif in_s2:
                    cell_content = f"{BG_RIGHT}{TEXT_WHITE}{formatted_cell}{RESET}"

                row_str_parts.append(cell_content)

            print("".join(row_str_parts))
        print()

