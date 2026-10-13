"""Parameter regressions for the actual PS2 notebook recurrence."""
import json
import unittest
from pathlib import Path

import numpy as np


class GovernmentShock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        notebook = json.loads((Path(__file__).parents[1] / "PS2_512.ipynb").read_text())
        source = next("".join(c["source"]) for c in notebook["cells"]
                      if c["cell_type"] == "code" and
                      "def y_stochastic_g(" in "".join(c["source"]))
        # Execute the notebook function, excluding its plotting invocation.
        source = source[:source.rfind("plot_y_stochastic(y_stochastic_g(")]
        namespace = {"np": np, "a": 0.5, "b": 0.2,
                     "categorize_solution": lambda *args: None}
        exec(compile(source, "PS2_512.ipynb:government-shock", "exec"), namespace)
        cls.recurrence = staticmethod(namespace["y_stochastic_g"])

    def check_path(self, g, duration, expected):
        result = self.recurrence(y_0=0, y_1=0, α=0.5, β=0.2, γ=1,
                                 n=5, σ=0, g=g, g_t=3, duration=duration)
        np.testing.assert_allclose(result, expected)
        self.assertTrue(np.isfinite(result).all())

    def test_no_government_spending(self):
        self.check_path(0, "one-off", [0, 0, 1, 1.7, 1.99])

    def test_constant_government_spending(self):
        self.check_path(2, None, [0, 0, 3, 5.1, 5.97])

    def test_one_off_shock(self):
        self.check_path(2, "one-off", [0, 0, 1, 3.7, 3.39])

    def test_permanent_shock(self):
        self.check_path(2, "permanent", [0, 0, 1, 3.7, 5.39])


if __name__ == "__main__":
    unittest.main()
