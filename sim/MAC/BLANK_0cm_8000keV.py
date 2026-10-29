"""Job BLANK_0cm_8000keV: mẫu BLANK, bề dày 0 cm, năng lượng 8000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="BLANK", thickness_cm=0.0, energy_kev=8000.0, primaries=@PRIMARIES@)
