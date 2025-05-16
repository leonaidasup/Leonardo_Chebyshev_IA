from numpy import cos, arccos

class Chebyshev_polynomials:
    def __init__(self,
                alpha: float,
                beta: float,
                interval: tuple[float, float],
                ARRAY_omega: dict[int, float]) -> None:
        self.alpha: float = alpha
        self.beta: float = beta
        self.interval: tuple[float, float] = interval
        self.ARRAY_omega: dict[int, float] = ARRAY_omega
    
    def MAP_f(self, ARRAY_x):
        result = []