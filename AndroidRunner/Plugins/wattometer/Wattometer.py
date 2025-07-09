import json
import os.path as op
from urllib import request

from AndroidRunner.Plugins.Profiler import Profiler


class Wattometer(Profiler):
    """Profiler for a Wattometer device exposing an HTTP API."""

    def __init__(self, config, paths):
        super(Wattometer, self).__init__(config, paths)
        self.ip = config.get("ip", "192.168.4.1")
        self.port = config.get("port", 80)
        self.output_dir = ""

    def _base_url(self):
        return f"http://{self.ip}:{self.port}" if self.port else f"http://{self.ip}"

    def start_profiling(self, device, **kwargs):
        try:
            request.urlopen(f"{self._base_url()}/startMeasures")
        except Exception as exc:  # pragma: no cover - network errors are ignored
            self.logger.warning(f"Failed to start wattometer measures: {exc}")

    def stop_profiling(self, device, **kwargs):
        try:
            request.urlopen(f"{self._base_url()}/stopMeasures")
        except Exception as exc:  # pragma: no cover - network errors are ignored
            self.logger.warning(f"Failed to stop wattometer measures: {exc}")

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

    def aggregate_subject(self):  # pragma: no cover - optional
        return

    def aggregate_end(self, data_dir, output_file):  # pragma: no cover - optional
        return