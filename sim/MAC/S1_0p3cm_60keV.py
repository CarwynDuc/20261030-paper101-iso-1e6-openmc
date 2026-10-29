"""Job S1_0p3cm_60keV: mẫu S1, bề dày 0.3 cm, năng lượng 60 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=0.3, energy_kev=60.0, primaries=@PRIMARIES@)
