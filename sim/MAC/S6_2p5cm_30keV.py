"""Job S6_2p5cm_30keV: mẫu S6, bề dày 2.5 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=2.5, energy_kev=30.0, primaries=@PRIMARIES@)
