"""Job S3_0p005cm_30keV: mẫu S3, bề dày 0.005 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=0.005, energy_kev=30.0, primaries=@PRIMARIES@)
