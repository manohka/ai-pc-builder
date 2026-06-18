from app.recommendation_engine.build_generator import BuildGenerator


generator = BuildGenerator()

build = generator.generate_build(
    "5060"
)

print(build)
