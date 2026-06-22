from app.recommendation_engine.build_generator import BuildGenerator


generator = BuildGenerator()

builds = generator.generate_builds(
    "5060"
)

for build in builds:

    print(build)
