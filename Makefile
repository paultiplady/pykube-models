

.PHONY: build
build: src/models

src/models: swagger.json
	datamodel-codegen  --input swagger.json --input-file-type jsonschema --output src/models/

swagger.json:
	curl -LOs https://raw.githubusercontent.com/kubernetes/kubernetes/v1.22.0/api/openapi-spec/swagger.json

.PHONY: clean
clean:
	rm -rf src/models
	rm -f swagger.json
