from matplotlib.axes import Axes
from matplotlib.colors import Colormap

from ._core import _SetupImage


def imgplot(
    data,
    ax=None,
    cmap=None,
    vmin=None,
    vmax=None,
    dx=None,
    units=None,
    cbar=True,
    cbar_label=None,
    cbar_fontdict=None,
    cbar_ticks=None,
    showticks=False,
    title=None,
    title_fontdict=None,
):

    # add vmin, vmax, dx, units to checks
    if cmap is not None:
        if not isinstance(cmap, str) or not isinstance(cmap, Colormap):
            raise TypeError
    if ax is not None:
        if not isinstance(ax, Axes):
            raise TypeError
    if not isinstance(cbar, bool):
        raise TypeError
    if cbar_label is not None:
        if not isinstance(cbar_label, str):
            raise TypeError
    if cbar_fontdict is not None:
        if not isinstance(cbar_fontdict, dict):
            raise TypeError
    if not isinstance(showticks, bool):
        raise TypeError
    if title is not None:
        if not isinstance(title, str):
            raise TypeError
    if title_fontdict is not None:
        if not isinstance(title_fontdict, dict):
            raise TypeError

    img_plotter = _SetupImage(
        data=data,
        ax=ax,
        cmap=cmap,
        vmin=vmin,
        vmax=vmax,
        dx=dx,
        units=units,
        cbar=cbar,
        cbar_label=cbar_label,
        cbar_fontdict=cbar_fontdict,
        cbar_ticks=cbar_ticks,
        showticks=showticks,
        title=title,
        fontdict=title_fontdict,
    )

    f, ax = img_plotter.plot()

    return f, ax, data
