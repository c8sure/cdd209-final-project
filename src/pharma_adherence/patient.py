import pandas as pd

class PatientAdherenceProfile:
    def __init__(self, patient_id, df: pd.DataFrame):
        self.patient_id = patient_id
        self.df = df.sort_values("fill_date")

    def total_fills(self):
        #TODO: Calculate and return the total number of fills?
        pass

    def average_copay(self):
        #TODO: Calculate and return the average copay_amount
        pass

    def average_days_supply(self):
        #TODO: Calculate and return the average days_supply
        pass

    def calculate_pdc(self):
        #TODO: Calculate and return the average proportion_days_covered (pdc)
        pass

    def is_adherent(self, threshold=0.75):
        #TODO: Return True if average pdc meets the adherence threshold provided
        pass

    def summary(self):
        return {
            "patient_id": self.patient_id,
            "total_fills": self.total_fills(),
            "avg_copay": self.average_copay(),
            "avg_days_supply": self.average_days_supply(),
            "pdc": self.calculate_pdc(),
            "adherent": self.is_adherent(),
        }
        