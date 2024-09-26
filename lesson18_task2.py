"""
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property boss, and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his
own workers. You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute,
use getters and setters instead!
"""

from typing import List, Optional


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: 'Boss'):
        self.id = id_
        self.name = name
        self.company = company
        self._boss: Optional['Boss'] = None
        self.boss = boss

    @property
    def boss(self) -> Optional['Boss']:
        return self._boss

    @boss.setter
    def boss(self, new_boss: 'Boss') -> None:
        if not isinstance(new_boss, Boss):
            raise ValueError("Boss must be an instance of Boss.")
        if self._boss is not None and self._boss != new_boss:
            self._boss.remove_worker(self)
        self._boss = new_boss
        new_boss.add_worker(self)


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers: List[Worker] = []

    @property
    def workers(self) -> List[Worker]:
        return self._workers

    def add_worker(self, worker: Worker) -> None:
        if not isinstance(worker, Worker):
            raise ValueError("Only instances of Worker can be added.")
        if worker.boss is not self:
            raise ValueError("Worker's boss must be the current instance.")
        if worker not in self._workers:
            self._workers.append(worker)

    def remove_worker(self, worker: Worker) -> None:
        if worker in self._workers:
            self._workers.remove(worker)
