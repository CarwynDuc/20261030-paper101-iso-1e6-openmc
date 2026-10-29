"""Job S3_2p5cm_300keV: mẫu S3, bề dày 2.5 cm, năng lượng 300 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=2.5, energy_kev=300.0, primaries=@PRIMARIES@)
