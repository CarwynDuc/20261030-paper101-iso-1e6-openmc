"""Job S5_2p5cm_1000keV: mẫu S5, bề dày 2.5 cm, năng lượng 1000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=2.5, energy_kev=1000.0, primaries=@PRIMARIES@)
