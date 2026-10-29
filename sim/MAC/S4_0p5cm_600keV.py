"""Job S4_0p5cm_600keV: mẫu S4, bề dày 0.5 cm, năng lượng 600 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=0.5, energy_kev=600.0, primaries=@PRIMARIES@)
