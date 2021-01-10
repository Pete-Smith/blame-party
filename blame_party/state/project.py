from .column import ColumnState
from .entry import EntryState
from .swimlane import SwimlaneState

EntryList = list[EntryState]
IndexList = list[int]
IndexGrid = list[list[int]]  # Column, Swimlane, Sort Order
ColumnList = list[ColumnState]
SwimlaneList = list[SwimlaneState]


class ProjectState:
    def __init__(self):
        self.entries = EntryList()
        self.outline = IndexList()
        self.board = IndexGrid()
        self.columns = ColumnList()
        self.swimlanes = SwimlaneList()
