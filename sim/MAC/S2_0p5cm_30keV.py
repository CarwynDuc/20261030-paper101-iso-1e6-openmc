"""Job S2_0p5cm_30keV: mẫu S2, bề dày 0.5 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=0.5, energy_kev=30.0, primaries=@PRIMARIES@)
