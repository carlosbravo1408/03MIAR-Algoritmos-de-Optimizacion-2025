from matplotlib import pyplot as plt


def add_water_mark(
        text: str,
        ax: plt.Axes,
        x: float = 0.98,
        y: float = 0.02,
        fontsize: int = 10,
        color: str = "white",
) -> plt.Axes:
    ax.text(
        x, y,
        text,
        fontsize=fontsize,
        transform=ax.transAxes,
        color=color,
        alpha=0.25,
        ha='right',
        va='bottom',
        fontweight='bold',
    )
    return ax
