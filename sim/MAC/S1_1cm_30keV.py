"""Job S1_1cm_30keV: mẫu S1, bề dày 1 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=1.0, energy_kev=30.0, primaries=@PRIMARIES@)
