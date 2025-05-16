from numpy import cos, arccos, zeros, ndarray

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
    
    def MAP_f(self, ARRAY_x: ndarray):
        ARRAY_x = (2 * ARRAY_x - self.beta) / self.alpha
        result: float = zeros(ARRAY_x.shape)
        for i, omega in ARRAY_omega:
            result += omega * cos(i * arccos(ARRAY_x))
        return result
    
    def f(self, x: float) -> float:
        x: float = (2 * x - self.beta) / self.alpha
        result: float = 0.0
        for i, omega in ARRAY_omega:
            result += omega * cos(i * arccos(x))
        return result
