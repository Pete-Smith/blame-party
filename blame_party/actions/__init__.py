import abc
import dataclasses

from ..state.project import ProjectState


class KanbanError(Exception):
    pass


class ChangeReport:
    """
    Report which entries on the outline or the board have been changed.
    This will be used to notify the user interface of changes.
    """
    pass


@dataclasses.dataclass
class Action(abc.ABC):
    timestamp: str
    user: str

    @abc.abstractmethod
    def validate(self, project: ProjectState) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def apply(self, project: ProjectState) -> ChangeReport:
        raise NotImplementedError()

    def unpack(self):
        """
        Return a tuple of values to persist to the on-disk project log.
        This will be the Action class name,
        followed by data field name & value pairs.
        """
        retval = [
            self.__class__.__name__, 'timestamp', self.timestamp, 'user',
            self.user
        ]
        for field in dataclasses.fields(self):
            if field.name in ('timestamp', 'user'):
                continue
            if field.type not in (str, int, float):
                raise TypeError('Action subclass data types may only be string'
                                ' and numerical types.')
            retval.extend((field.name, getattr(self, field.name)))
        return retval
