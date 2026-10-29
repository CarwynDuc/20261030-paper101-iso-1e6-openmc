"""Job S3_0p8cm_15keV: mẫu S3, bề dày 0.8 cm, năng lượng 15 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=0.8, energy_kev=15.0, primaries=@PRIMARIES@)
