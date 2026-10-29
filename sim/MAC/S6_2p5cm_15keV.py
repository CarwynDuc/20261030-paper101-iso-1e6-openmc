"""Job S6_2p5cm_15keV: mẫu S6, bề dày 2.5 cm, năng lượng 15 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=2.5, energy_kev=15.0, primaries=@PRIMARIES@)
