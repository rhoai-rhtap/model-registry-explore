package repositories

// Repositories struct is a single convenient container to hold and represent all our repositories.
type Repositories struct {
	HealthCheck         *HealthCheckRepository
	ModelRegistry       *ModelRegistryRepository
	ModelRegistryClient ModelRegistryClientInterface
}

func NewRepositories(modelRegistryClient ModelRegistryClientInterface) *Repositories {
	return &Repositories{
		HealthCheck:         NewHealthCheckRepository(),
		ModelRegistry:       NewModelRegistryRepository(),
		ModelRegistryClient: modelRegistryClient,
	}
}