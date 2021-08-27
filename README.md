# pykube-models

Pydantic models generated from the Kubernetes API, for the [pykube](https://pykube.readthedocs.io/en/latest/) k8s client.

## Rationale

The official [Python client for Kubernetes](https://github.com/kubernetes-client/python/blob/master/examples/deployment_create.py)
is based on the [OpenAPI Client Generator](https://github.com/OpenAPITools/openapi-generator).
I find the auto-generated client to be quite un-ergonomic to work with, and it doesn't include any of the modern Python
type-hinting features that make for easy to use IDE integrations.

Pykube provides a simple Python client with some nice Django-like utilities, which make it quite nice to work with for
simple workflows. However it doesn't have any knowledge of the Kubernetes OpenAPI spec, just a few basic classes that
are hand-coded like Deployment. These hand-coded classes take an `obj` dictionary and so there's also no type 
hinting.

Pydantic provides nice type-hint-enabled data models which can be generated from OpenAPI specs.
It should be possible to generate a set of Pydantic models once per k8s version, and use these to render the spec dict 
that Pykube expects.

# TODO

- [ ] Figure out Pydantic constructor type hinting
  - Should be able to do this in mypy like: https://pydantic-docs.helpmanual.io/mypy_plugin/#generate-a-signature-for-model__init__
    - Couldn't get this set up immediately
  - Can also get this done with PyCharm plugin: https://pydantic-docs.helpmanual.io/pycharm_plugin/
- [ ] Full mypy testing?
- [ ] Figure out / report datamodel-code-generator bug: no packages for some generated modules, just the leaf modules.
- [ ] Set up a pypi package?
  - https://flit.readthedocs.io/en/latest/
  - https://packaging.python.org/tutorials/packaging-projects/
- [ ] Define dependencies (poetry? setup.cfg?)
  - datamodel-code-generator
  - pytest
  - mypy
- [ ] Test strategy?
  - VCRPY?
  - GH Actions?
  - Revisit pytest - had to add conftest.py to src/models to get pytest to find the src/ modules.
- [ ] Investigate baking in the apiVersion/kind to the base models; shouldn't need to re-specify.
  - Maybe could use a different base class? In datamodel-code-generator:
    --base-class BASE_CLASS
                        Base Class (default: pydantic.BaseModel)
- [ ] Strategy for versioning? Probably want to support different k8s API versions.
    