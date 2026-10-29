"""Job S4_2cm_4000keV: mẫu S4, bề dày 2 cm, năng lượng 4000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=2.0, energy_kev=4000.0, primaries=@PRIMARIES@)
