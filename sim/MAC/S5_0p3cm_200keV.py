"""Job S5_0p3cm_200keV: mẫu S5, bề dày 0.3 cm, năng lượng 200 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.3, energy_kev=200.0, primaries=@PRIMARIES@)
