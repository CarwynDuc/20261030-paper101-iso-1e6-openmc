"""Job S1_0p5cm_800keV: mẫu S1, bề dày 0.5 cm, năng lượng 800 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=0.5, energy_kev=800.0, primaries=@PRIMARIES@)
