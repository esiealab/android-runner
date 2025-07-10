from urllib import request, parse
from AndroidRunner.Plugins.Profiler import Profiler

class Wattometer(Profiler):
    """Plugin to control the Watto-Meter power measurement board."""

    def __init__(self, config, paths):
        super(Wattometer, self).__init__(config, paths)
        self.ip = config.get('ip')
        self.device_name = config.get('experiment_name', '')
        self.output_dir = ''

    def dependencies(self):
        return []

    def load(self, device):
        return

    def start_profiling(self, device, **kwargs):
        if self.ip is None:
            return
        name = self.device_name or kwargs.get('experiment_name', '')
        query = parse.urlencode({'device': name})
        url = f"http://{self.ip}/startMeasures?{query}"
        try:
            request.urlopen(url, timeout=5)
        except Exception as exc:
            self.logger.warning(f"Wattometer start failed: {exc}")

    def stop_profiling(self, device, **kwargs):
        if self.ip is None:
            return
        url = f"http://{self.ip}/stopMeasures"
        try:
            request.urlopen(url, timeout=5)
        except Exception as exc:
            self.logger.warning(f"Wattometer stop failed: {exc}")

    def collect_results(self, device):
        return

    def unload(self, device):
        return

    def set_output(self, output_dir):
        self.output_dir = output_dir

    def aggregate_subject(self):
        return

    def aggregate_end(self, data_dir, output_file):
        return
