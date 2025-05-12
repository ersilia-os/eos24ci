FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia


RUN pip install rdkit==2022.3.3
RUN pip install joblib==1.1.0
RUN pip install drugtax==1.0.14
RUN pip install upsetplot==0.6.0 
RUN pip install pandas==1.1.5 
RUN pip install matplotlib==3.3.4
RUN pip install pubchempy==1.0.4



WORKDIR /repo
COPY . /repo
