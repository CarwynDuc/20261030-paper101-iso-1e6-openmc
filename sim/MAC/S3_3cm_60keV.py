"""Job S3_3cm_60keV: mẫu S3, bề dày 3 cm, năng lượng 60 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=3.0, energy_kev=60.0, primaries=@PRIMARIES@)
