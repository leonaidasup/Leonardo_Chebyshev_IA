from numpy import cos, arccos, zeros, ndarray, sign

class Walsh_chebyshev_wavelet:
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
        ARRAY_y: float = zeros(ARRAY_x.shape)
        for i, omega in ARRAY_omega:
            ARRAY_TEMP_y: float = zeros(ARRAY_x.shape)
            for j, d in enumerate(str(bin(i))[3:]):
                if d == 1:
                    ARRAY_TEMP_y *= sign(cos(2 * int(j) * arccos(ARRAY_x)))
            ARRAY_y += omega * ARRAY_TEMP_y
        return ARRAY_y
    
    def f(self, x: float) -> float:
        x: float = (2 * x - self.beta) / self.alpha
        y: float = 0.0
        for i, omega in ARRAY_omega:
            TEMP_y = 1.0
            for j, d in enumerate(str(bin(i))[3:]):
                if d == 1:
                    TEMP_y *= sign(cos(2 * int(j) * arccos(ARRAY_x)))
            y += omega * TEMP_y
        return y
