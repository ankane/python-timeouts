from .conftest import TestTimeouts
import numpy as np
import osqp
import scipy


class TestOsqp(TestTimeouts):
    def test_solve(self):
        P = scipy.sparse.coo_matrix(np.array([[4, 1], [0, 2]])).tocsc()
        q = np.array([1, 1])
        A = scipy.sparse.coo_matrix(np.array([[1, 1], [1, 0], [0, 1]])).tocsc()
        l = np.array([1, 0, 0])
        u = np.array([1, 0.7, 0.7])

        m = osqp.OSQP()
        m.setup(P=P, q=q, A=A, l=l, u=u, alpha=1.0, time_limit=0.000001)
        result = m.solve(raise_error=False)
        assert result.info.status == 'run time limit reached'
