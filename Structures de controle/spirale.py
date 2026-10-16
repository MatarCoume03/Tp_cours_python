import math
xa ,ya = 0, 0
θ = 0
r = 0.5
while  θ <= 4*(math.pi):
    xa = math.cos(θ) * r
    ya = math.sin(θ) * r
    θ += 0.1
    r += 0.1
    print(f"{xa:.5f}    {ya:.5f}")