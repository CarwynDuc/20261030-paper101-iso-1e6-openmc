"""Job S5_1cm_50keV: mẫu S5, bề dày 1 cm, năng lượng 50 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=1.0, energy_kev=50.0, primaries=@PRIMARIES@)
