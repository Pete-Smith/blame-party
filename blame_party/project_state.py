from blame_party.column_state import ColumnState
from blame_party.entry_state import EntryState
from blame_party.swimlane_state import SwimlaneState

EntryList = list[EntryState]
IndexList = list[int]
IndexGrid = list[list[int]]
ColumnList = list[ColumnState]
SwimlaneList = list[SwimlaneState]


class ProjectState:
    def __init__(self):
        self.entries = EntryList()
        self.outline = IndexList()
        self.board = IndexGrid()
        self.columns = ColumnList()
        self.swimlanes = SwimlaneList()
