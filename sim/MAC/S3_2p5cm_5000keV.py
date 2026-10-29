"""Job S3_2p5cm_5000keV: mẫu S3, bề dày 2.5 cm, năng lượng 5000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=2.5, energy_kev=5000.0, primaries=@PRIMARIES@)
