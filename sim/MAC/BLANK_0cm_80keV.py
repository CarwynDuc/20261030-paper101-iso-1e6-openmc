"""Job BLANK_0cm_80keV: mẫu BLANK, bề dày 0 cm, năng lượng 80 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="BLANK", thickness_cm=0.0, energy_kev=80.0, primaries=@PRIMARIES@)
