from dataclasses import dataclass
from . import Action, ChangeReport
from ..state.project import ProjectState
from ..state.entry import EntryState


@dataclass
class NewEntry(Action):
    markdown: str

    def validate(self, project: ProjectState) -> bool:
        return bool(self.markdown.strip())

    def apply(self, project: ProjectState) -> ChangeReport:
        report = ChangeReport()
        entry = EntryState()
        project.entries.append(entry)
        return report
