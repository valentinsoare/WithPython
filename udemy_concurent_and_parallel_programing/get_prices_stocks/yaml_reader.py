# yaml_reader.py

import yaml
import importlib
from multiprocessing import Queue


class YamlReaderExecutor:
    def __init__(self, filename: str):
        self.filename: str = filename
        self._queues: dict = {}
        self._workers: dict = {}

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    def _load_yaml_doc(self):
        with open(file=self.filename, mode='r') as inFile:
            self.yaml_data = yaml.safe_load(inFile)

    def _initialize_queues(self):
        for i in self.yaml_data['queues']:
            queue_name = i['name']
            self._queues[queue_name] = Queue()

    def _initialize_workers(self):
        for j in self.yaml_data['workers']:
            WorkerClass = getattr(importlib.import_module(j['location']), j['class'])
            input_queue = j.get('input_queue')
            output_queue = j.get('output_queue')
            worker_name = j['name']
            num_instances = j.get('instances', 1)

            init_params = {
                'input_queue': self._queues[input_queue] if input_queue else None,
                'output_queues': [self._queues[j] for j in output_queue] if output_queue else None
            }

            self._workers[worker_name] = []
            for i in range(num_instances):
                self._workers[worker_name].append(WorkerClass(**init_params))

    def _join_workers(self):
        for k in self._workers:
            for l in self._workers[k]:
                l.join()

    def process_doc(self):
        self._load_yaml_doc()
        self._initialize_queues()
        self._initialize_workers()
        #self._join_workers()
