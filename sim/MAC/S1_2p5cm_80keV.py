"""Job S1_2p5cm_80keV: mẫu S1, bề dày 2.5 cm, năng lượng 80 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=2.5, energy_kev=80.0, primaries=@PRIMARIES@)
