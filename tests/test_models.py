import pykube
import pytest
import yaml

from models.io.k8s.api.apps.v1 import Deployment, DeploymentSpec
from models.io.k8s.api.core.v1 import PodTemplateSpec, PodSpec, Container, ContainerPort
from models.io.k8s.apimachinery.pkg.apis.meta.v1 import LabelSelector, ObjectMeta


def test_simple_deployment():
    """Test that we can generate a simple Deployment from the K8s docs.

    The k8s Deployment docs:
    https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment
    Give a simple spec. Recreate this as a first test of the Pydantic models.
    """
    deployment = Deployment(
        # WIBNI this was baked in; it should be hard-coded for each Pydantic model.
        apiVersion='apps/v1',
        # WIBNI this was baked in; it should be hard-coded for each Pydantic model.
        kind='Deployment',
        metadata=ObjectMeta(
            name='nginx-deployment',
            labels={'app': 'nginx'}
        ),
        spec=DeploymentSpec(
            replicas=3,
            selector=LabelSelector(matchLabels={'app': 'nginx'}),
            template=PodTemplateSpec(
                metadata=ObjectMeta(
                    labels={'app': 'nginx'},
                ),
                spec=PodSpec(
                    containers=[
                        Container(
                            name='nginx',
                            image='nginx:1.14.2',
                            ports=[
                                ContainerPort(containerPort=80)
                            ]
                        )
                    ]
                )
            )
        )
    )

    docs_yaml = """
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-deployment
      labels:
        app: nginx
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.14.2
            ports:
            - containerPort: 80
    """
    docs_dict = yaml.load(docs_yaml)

    assert deployment.dict(skip_defaults=True) == docs_dict


@pytest.mark.skip
def test_pykube_deployment():
    """Test that we can pass a DeploymentSpec to a Pykube deployment."""
    api = pykube.HTTPClient(config=pykube.KubeConfig.from_file())
    pykube.Deployment(api=api, obj=DeploymentSpec().dict(skip_defaults=True))
