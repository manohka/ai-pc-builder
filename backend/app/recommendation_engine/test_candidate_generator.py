from app.recommendation_engine.candidate_generator import CandidateGenerator


generator = CandidateGenerator()

results = generator.generate("5060")

for component in results:

    print(component.name)
