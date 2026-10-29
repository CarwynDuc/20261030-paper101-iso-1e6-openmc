"""Job S6_1p5cm_50keV: mẫu S6, bề dày 1.5 cm, năng lượng 50 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=1.5, energy_kev=50.0, primaries=@PRIMARIES@)
