"""Job S4_2cm_300keV: mẫu S4, bề dày 2 cm, năng lượng 300 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=2.0, energy_kev=300.0, primaries=@PRIMARIES@)
