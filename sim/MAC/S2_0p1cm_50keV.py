"""Job S2_0p1cm_50keV: mẫu S2, bề dày 0.1 cm, năng lượng 50 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=0.1, energy_kev=50.0, primaries=@PRIMARIES@)
