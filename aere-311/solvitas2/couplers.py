from coupler import *
from hoppers import *
from utils import *


class NormalShockNozzle(Coupler):
    def __init__(self, invariants, state1, state_e):
        _Ae_At1 = invariants[Ae_At]
        _A1_At1 = (_Ae_At1 - 1) / 2 + 1

        pre_shock = PerfectlyExpandedSupersonicNozzle(
            {
                **invariants,
                **state1,
                A_At: _A1_At1,
            }
        ).knowns

        shock = NormalShock(
            {
                **invariants,
                **to_state_space(pre_shock, "generic", 1),
            }
        ).knowns

        post_shock_state_space = to_state_space(shock, 2, "generic")
        post_shock_back = PerfectlyExpandedSubsonicNozzle(
            {
                **invariants,
                **post_shock_state_space,
            }
        ).knowns

        _A1_At2 = post_shock_back[A_At]
        _Ae_At2 = _Ae_At1 / _A1_At1 * _A1_At2

        post_shock_forward = PerfectlyExpandedSubsonicNozzle(
            {
                **invariants,
                # **post_shock_state_space,
                A_At: _Ae_At2,
            }
        ).knowns

        _Me = post_shock_forward[M]
