"""Job S3_0p1cm_20keV: mẫu S3, bề dày 0.1 cm, năng lượng 20 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=0.1, energy_kev=20.0, primaries=@PRIMARIES@)
