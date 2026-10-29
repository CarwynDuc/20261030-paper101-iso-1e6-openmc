"""Job S7_2cm_1000keV: mẫu S7, bề dày 2 cm, năng lượng 1000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=2.0, energy_kev=1000.0, primaries=@PRIMARIES@)
