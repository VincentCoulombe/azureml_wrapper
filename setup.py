import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="azureml_wrapper",
    version="0.0.1",
    author="Vincent Coulombe",
    author_email="vincent.coulombe@syntell.com",
    description="Wrapper autour du azureml-sdk.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VincentCoulombe/azureml_wrapper.git",
    license="MIT",
    py_modules=["PipelineWrapper.py", "PipelineStep.py", "WorkspaceWrapper.py"],
    install_requires=["azureml.core", "azureml.data", "azureml.pipeline", "azureml.exceptions"]
)