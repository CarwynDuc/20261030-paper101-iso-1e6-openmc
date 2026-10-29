"""Job S7_1cm_300keV: mẫu S7, bề dày 1 cm, năng lượng 300 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=1.0, energy_kev=300.0, primaries=@PRIMARIES@)
