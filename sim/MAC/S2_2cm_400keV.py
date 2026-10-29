"""Job S2_2cm_400keV: mẫu S2, bề dày 2 cm, năng lượng 400 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=2.0, energy_kev=400.0, primaries=@PRIMARIES@)
