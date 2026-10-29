"""Job S2_2cm_60keV: mẫu S2, bề dày 2 cm, năng lượng 60 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=2.0, energy_kev=60.0, primaries=@PRIMARIES@)
