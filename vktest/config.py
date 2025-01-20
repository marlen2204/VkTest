# Глубина очереди (iodepth)
IODEPTH_VALUES = [1, 2, 4, 8, 16, 32, 64, 128, 256]

# Базовые параметры fio
FIO_BASE_PARAMS = [
    "--ioengine=libaio",
    "--direct=1",
    "--bs=4k",
    "--size=1G",
    "--numjobs=1",
    "--output-format=json",
    "--runtime=30"
]
