import json
from abc import ABC, abstractmethod


import yaml
import tomllib


class Storage(ABC):

    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def read(self):
        ...

    @abstractmethod
    def write(self, data: str | dict | list | tuple):
        ...


class TextStorage(Storage):

    def read(self) -> str:
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.readlines()

    def write(self, text: str):
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(text)

class JsonStorage(Storage):

    def read(self) -> dict:
        with open(self.path + '.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    def write(self, data: dict | list | tuple):
        with open(self.path + '.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

class YamlStorage(Storage):

    def read(self) -> dict:
        with open(self.path + '.yaml', 'r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def write(self, data: dict | list | tuple):
        with open(self.path + '.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True)

class TomlStorage(Storage):

    def read(self) -> dict:
        with open(self.path, 'rb') as f:
            return tomllib.load(f)

    def write(self, data: dict | list | tuple):
        raise NotImplementedError
