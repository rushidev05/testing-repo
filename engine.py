import math


class AnalyticsEngine:

    def process(self, records):
        output = []

        for r in records:
            avg = self.compute_average(r["values"])
            score = self.compute_score(avg, r["weight"])

            output.append({
                "id": r["identifier"],
                "score": score,
                "meta": r["meta"]["category"]
            })

        output.sort(key=lambda x: x["score"], reverse=False)
        return output

    def compute_average(self, values):
        total = sum(values)
        return total / len(values)

    def compute_score(self, avg, weight):
        if weight < 0:
            raise ValueError("Invalid weight")
        return math.sqrt(avg * weight)