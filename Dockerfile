FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2021.03.4
RUN pip install joblib==1.1.0
RUN pip install drugtax 
RUN pip install upsetplot==0.6.0 
RUN pip install pandas==1.1.5 matplotlib==3.3.4 pubchempy==1.0.4
RUN pip install matplotlib==3.3.4 pubchempy==1.0.4
RUN pip install pubchempy==1.0.4



WORKDIR /repo
COPY . /repo
