from matplotlib.testing.decorators import image_comparison

from mock_utils import FakeDataReader
from postprocessing import make_figure_2

TOL = 0


@image_comparison(baseline_images=['mock_figure_2'], extensions=['png', 'pdf'], tol=TOL)
def test__make_figure_2():
    data_reader = FakeDataReader()
    fig = make_figure_2(data_reader)
