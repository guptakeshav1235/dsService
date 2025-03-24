from setuptools import setup, find_packages

install_requires = [
    "Flask==3.1.0",
    "kafka_python==2.1.2",
    "langchain_core==0.3.47",
    "langchain_mistralai==0.2.9",
    "langchain_openai==0.3.9",
    "pydantic==2.10.6",
    "python-dotenv==1.0.1",
]
setup(
    name="ds-service",
    version="1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    include_package_data=True,
)
