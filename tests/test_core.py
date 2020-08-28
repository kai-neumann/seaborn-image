import pytest

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

import seaborn_image as isns

matplotlib.use("AGG")  # use non-interactive backend for tests


data = np.random.random(2500).reshape((50, 50))


def test_setup_figure():
    img_setup = isns._core._SetupImage(data)
    f, ax = img_setup._setup_figure()

    assert isinstance(f, Figure)
    assert isinstance(ax, Axes)


def test_setup_figure_check_title_dict():
    with pytest.raises(TypeError):
        img_setup = isns._core._SetupImage(data, title_dict=[{"fontsize": 20}])
        f, ax = img_setup._setup_figure()


def test_setup_scalebar():
    with pytest.raises(AttributeError):
        img_setup = isns._core._SetupImage(data, dx=1)
        f, ax = img_setup._setup_figure()
        img_setup._setup_scalebar(ax)


def test_setup_scalebar_dimension():
    with pytest.raises(ValueError):
        img_setup = isns._core._SetupImage(
            data, dx=1, units="nm", dimension="imperial-reciprocal"
        )
        f, ax = img_setup._setup_figure()
        img_setup._setup_scalebar(ax)


def test_cbar_orientation():
    with pytest.raises(ValueError):
        img_setup = isns._core._SetupImage(data, cbar=True, orientation="right")
        f, ax, cax = img_setup.plot()


def test_plot_check_cbar_dict():
    with pytest.raises(TypeError):
        img_setup = isns._core._SetupImage(
            data, cbar=True, cbar_fontdict=[{"fontsize": 20}]
        )
        f, ax, cax = img_setup.plot()


def test_data_plotted_is_same_as_input():
    img_setup = isns._core._SetupImage(data)
    f, ax, cax = img_setup.plot()

    # check if data iput is what was plotted
    np.testing.assert_array_equal(ax.images[0].get_array().data, data)

    plt.close("all")


@pytest.mark.parametrize(
    "cmap", [None, "acton"]
)  # test if seaborn-image supplied cmaps are working
@pytest.mark.parametrize(
    "dx, units, dimension",
    [(None, None, None), (1, "nm", "si"), (1, "1/um", "si-reciprocal")],
)
@pytest.mark.parametrize("cbar", [True, False])
@pytest.mark.parametrize("orientation", ["horizontal", "h", "vertical", "v"])
@pytest.mark.parametrize("showticks", [True, False])
@pytest.mark.parametrize("despine", [True, False])
def test_plot_w_all_inputs(
    cmap, cbar, dx, units, dimension, orientation, showticks, despine
):
    img_setup = isns._core._SetupImage(
        data,
        cmap=cmap,
        vmin=None,
        vmax=None,
        title="My Title",
        fontdict={"fontsize": 20},
        dx=dx,
        units=units,
        dimension=dimension,
        cbar=cbar,
        orientation=orientation,
        cbar_fontdict={"fontsize": 20},
        cbar_label="cbar label",
        cbar_ticks=[],
        showticks=showticks,
        despine=despine,
    )
    f, ax, cax = img_setup.plot()

    assert isinstance(f, Figure)
    assert isinstance(ax, Axes)
    if cbar is True:
        assert isinstance(cax, Axes)
    else:
        assert cax is None

    plt.close("all")