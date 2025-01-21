import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, output_file):
        self.output_file = output_file

    def plot_latency_vs_iodepth(self, results):
        """
        Создает PNG-график зависимости latency от iodepth.
        """
        plt.figure(figsize=(10, 6))

        for rw, data in results.items():
            if data:
                iodepths, latencies = zip(*data)
                plt.plot(iodepths, latencies, label=rw)

        plt.title("Latency vs IODEPTH")
        plt.xlabel("IODEPTH")
        plt.ylabel("Latency (usec)")
        plt.legend()
        plt.grid(True)
        plt.savefig(self.output_file)
        print(f"График сохранен в {self.output_file}")
