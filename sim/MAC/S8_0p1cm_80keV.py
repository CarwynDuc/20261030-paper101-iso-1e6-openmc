"""Job S8_0p1cm_80keV: mẫu S8, bề dày 0.1 cm, năng lượng 80 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=0.1, energy_kev=80.0, primaries=@PRIMARIES@)
