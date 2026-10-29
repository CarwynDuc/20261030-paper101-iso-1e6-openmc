"""Job S8_0p1cm_8000keV: mẫu S8, bề dày 0.1 cm, năng lượng 8000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=0.1, energy_kev=8000.0, primaries=@PRIMARIES@)
