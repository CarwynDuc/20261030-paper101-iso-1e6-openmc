"""Job S2_2p5cm_200keV: mẫu S2, bề dày 2.5 cm, năng lượng 200 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=2.5, energy_kev=200.0, primaries=@PRIMARIES@)
