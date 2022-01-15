from .conftest import TestTimeouts
import numpy as np
import scipy
import scs


class TestScs(TestTimeouts):
    def test_solve(self):
        A = scipy.sparse.csc_matrix([[1.], [-1.]])
        b = np.array([1., 0.])
        c = np.array([-1.])

        data = {'A': A, 'b': b, 'c': c}
        cone = {'l': 2}

        sol = scs.solve(data, cone, time_limit_secs=0.000001, verbose=False)
        assert sol['info']['status'] == 'solved (inaccurate - reached time_limit_secs)'
