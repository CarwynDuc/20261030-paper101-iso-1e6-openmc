"""Job S8_1p5cm_30keV: mẫu S8, bề dày 1.5 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=1.5, energy_kev=30.0, primaries=@PRIMARIES@)
