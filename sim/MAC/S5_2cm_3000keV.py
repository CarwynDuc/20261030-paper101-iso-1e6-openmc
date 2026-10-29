"""Job S5_2cm_3000keV: mẫu S5, bề dày 2 cm, năng lượng 3000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=2.0, energy_kev=3000.0, primaries=@PRIMARIES@)
