"""Job S7_0p5cm_400keV: mẫu S7, bề dày 0.5 cm, năng lượng 400 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=0.5, energy_kev=400.0, primaries=@PRIMARIES@)
