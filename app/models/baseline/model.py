import json
import re

MAP_FILE = "app/models/baseline/artifacts/baseline_feat_map.json"

class NaiveMap:
    def __init__(self) -> None:
        self.map = json.load(open(MAP_FILE, 'r'))

    def annotate(self, case_num: int, patient_history: str) -> dict:
        """Simple annotate method to find feature tags in a given patient history"""
        pn_history = self.preprocess_text(patient_history)
        predictions = {}
        for feature in self.map[str(case_num)]:
            annotations = []
            locations = []
            
            for annotation in self.map[str(case_num)][feature]:
                if annotation in pn_history:
                    start_idx = pn_history.find(annotation)
                    end_idx = start_idx+len(annotation)
                    annotations.append(annotation)
                    locations.append(f'{start_idx} {end_idx}')
            
            predictions.update({
                feature: {
                    "annotation": annotations,
                    "location": locations
                }
            })

        return predictions

    def preprocess_text(seelf, text: str) -> str:
        """Basic text preprocessing to normalize text.
        Only `lower()` for now.

        Taken from eda_and_basline.ipynb
        """
        normalized_text = text.lower()
        
        return normalized_text