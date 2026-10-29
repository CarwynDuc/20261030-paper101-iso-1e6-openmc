"""Job S4_1cm_200keV: mẫu S4, bề dày 1 cm, năng lượng 200 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=1.0, energy_kev=200.0, primaries=@PRIMARIES@)
