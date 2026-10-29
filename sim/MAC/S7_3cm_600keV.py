"""Job S7_3cm_600keV: mẫu S7, bề dày 3 cm, năng lượng 600 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=3.0, energy_kev=600.0, primaries=@PRIMARIES@)
