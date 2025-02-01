from LocationToNote.ILocationToNote import ILocationToNote
from typing import List, Tuple

class AScaleLocationToNote(ILocationToNote):
    def __init__(self):
        # A major scale
        self.notes = [440, 493, 554, 587, 659, 739, 830, 880]

    def get_notes(self, source_locations: List[Tuple[int, int]]) -> List[int]:
        notes = []
        for light_x, light_y in source_locations:
            # Map the x location somewhat uniformly onto notes
            note = self.notes[min(max(0, int((light_x - 200)/100)), len(self.notes) - 1)]
            notes.append(note)
        return notes