"""Job S7_0p3cm_6000keV: mẫu S7, bề dày 0.3 cm, năng lượng 6000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=0.3, energy_kev=6000.0, primaries=@PRIMARIES@)
