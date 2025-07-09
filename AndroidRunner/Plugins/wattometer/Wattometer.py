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
        try:
            with request.urlopen(f"{self._base_url()}/listFiles") as resp:
                files = json.loads(resp.read().decode())
        except Exception as exc:  # pragma: no cover - network errors are ignored
            self.logger.warning(f"Failed to list wattometer files: {exc}")
            return

        if not files:
            self.logger.warning("No wattometer files found")
            return

        latest = max(files, key=lambda x: int(x.get("timestamp", 0)))
        filename = latest["name"]
        url = f"{self._base_url()}/downloadFile?file={filename}"
        dest = op.join(self.output_dir, filename)
        try:
            with request.urlopen(url) as resp, open(dest, "wb") as out_file:
                out_file.write(resp.read())
        except Exception as exc:  # pragma: no cover - network errors are ignored
            self.logger.warning(f"Failed to download wattometer file: {exc}")

    def unload(self, device):
        return

    def set_output(self, output_dir):
        self.output_dir = output_dir

    def aggregate_subject(self):
        return

    def aggregate_end(self, data_dir, output_file):
        return
