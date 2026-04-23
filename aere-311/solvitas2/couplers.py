from coupler import *
from hoppers import *


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

        _M1 = pre_shock[M]

        shock = NormalShock(
            {
                **invariants,
                # **to_state_space(pre_shock, "generic", 1),
                M1: _M1,
            }
        ).knowns

        _M2 = shock[M2]

        post_shock_back = PerfectlyExpandedSubsonicNozzle(
            {
                **invariants,
                M: _M2,
            }
        ).knowns

        _A1_At2 = post_shock_back[A_At]
        _Ae_At2 = _Ae_At1 / _A1_At1 * _A1_At2

        post_shock_forward = PerfectlyExpandedSubsonicNozzle(
            {
                **invariants,
                A_At: _Ae_At2,
            }
        ).knowns

        _Me = post_shock_forward[M]
